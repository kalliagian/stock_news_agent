from taipy.gui import Gui, invoke_long_callback, notify
import taipy.gui.builder as tgb
import pandas as pd
import json

from agent import NewsSummarizationAgent

agent = NewsSummarizationAgent("Kallia/t5-small-finetuned-stock-news")

categories = []
selected_category = []
selected_article = "Click on a summary to read the whole article."
data = pd.DataFrame.from_records([], columns=['Assets', 'News Summaries'])

def load_asset_list():
    with open("news_dataset/2020_processed.json", "r", encoding="utf-8") as f:
        dataset = json.load(f) 

    comps = set()

    for a in dataset:
        for comp in a['mentioned_companies']:
            comps.add(comp)

    comps = list(comps)
    comps.sort()
    return comps

categories = load_asset_list()

def get_summaries(categories):
    print(categories)

    # Fetch & summarize
    relevant_articles = agent.fetch_articles(categories)
    data = agent.summarize_articles(relevant_articles)
    print(categories)
    return data


def show_summaries_status(state, status, result):
    """
    Periodically update the status of the long callback.

    Args:
        state: The state of the application.
        status: The status of the long callback.
    """
    if isinstance(status, bool):
        if status:
            state.data = result
            state.selected_article = "Click on a summary to read the whole article."
            notify(state, "success", "Finished")
        else:
            notify(state, "error", "An error was raised")
    else:
        notify(state, "info", "Fetching and summarizing... Please wait")

def apply_changes(state):
    invoke_long_callback(
        state, get_summaries, [state.selected_category],
            show_summaries_status, [],
            5000
    )

def show_article_dialog(state, _, payload):
    selected_row_idx = payload['index']
    print(selected_row_idx)
    state.selected_article = state.data.loc[selected_row_idx, ['Articles']]['Articles']
    print(state.selected_article)



with tgb.Page() as page:
    with tgb.part(class_name="container"):
        tgb.text('### News Summaries on Portfolio Assets', mode='md')
        with tgb.part(class_name="card"):
            tgb.text("Choose Portfolio **Assets**", mode="md")
            with tgb.layout(columns="1 1"):
                with tgb.part():
                    tgb.selector(
                        value="{selected_category}",
                        lov=categories,
                        dropdown=True,
                        multiple=True
                    )
                with tgb.part(class_name="text-center"):
                    tgb.button(
                        "Apply",
                        class_name="plain apply_button",
                        on_action=apply_changes,
                        # class_name="fullwidth"
                    )

        tgb.html("br")
        tgb.table(data="{data}", columns=['Assets', 'News Summaries'], on_action=show_article_dialog)

        with tgb.part(class_name="card"):
            # tgb.text("Click on a summary to read the whole article.", mode="md")
            tgb.text("{selected_article}", mode="md")
            

if __name__ == "__main__":
    gui = Gui(page=page)
    # gui.on_init = load_asset_list
    gui.run(dark_mode=False, title="Portfolio news")
    