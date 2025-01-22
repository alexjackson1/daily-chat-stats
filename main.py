import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_openai_conversations(path: str):
    with open(path, "r") as f:
        data = json.load(f)

    records = []
    for datum in data:
        record = {}
        record["title"] = datum["title"]
        record["create_time"] = datum["create_time"]
        user_count = 0
        for item in datum["mapping"]:
            if "message" in datum["mapping"][item]:
                if datum["mapping"][item]["message"]:
                    if datum["mapping"][item]["message"]["author"]["role"] == "user":
                        user_count += 1

        record["user_messages"] = user_count

        records.append(record)

    return records


def read_anthropic_conversations(path: str):
    with open("anthropic/conversations.json") as f:
        data = json.load(f)

    records = []
    for datum in data:
        record = {}
        record["title"] = datum["name"]
        record["create_time"] = datum["created_at"]
        user_count = 0
        for item in datum["chat_messages"]:
            if item["sender"] == "human":
                user_count += 1

        record["user_messages"] = user_count

        records.append(record)

    return records


if __name__ == "__main__":
    openai_path = "openai/conversations.json"
    anthropic_path = "anthropic/conversations.json"

    openai_stats = read_openai_conversations(openai_path)
    anthropic_stats = read_anthropic_conversations(anthropic_path)

    openai_df = pd.DataFrame(openai_stats)
    anthropic_df = pd.DataFrame(anthropic_stats)

    openai_df["provider"] = "openai"
    anthropic_df["provider"] = "anthropic"

    openai_df["create_time"] = pd.to_datetime(openai_df["create_time"], unit="s")
    anthropic_df["create_time"] = pd.to_datetime(anthropic_df["create_time"])

    openai_df["create_time"] = openai_df["create_time"].dt.tz_localize("UTC")

    df = pd.concat([openai_df, anthropic_df])

    df["date"] = df["create_time"].dt.date
    daily_data = df.groupby(["date", "provider"])["user_messages"].sum().reset_index()

    plt.style.use("dark_background")
    plt.figure(figsize=(15, 7))
    ax = sns.barplot(
        data=daily_data,
        x="date",
        y="user_messages",
        hue="provider",
        palette=["#00A67E", "#ab562f"],
    )
    plt.xticks(rotation=45, ha="right")

    n = len(ax.get_xticklabels()) // 14
    if n > 0:
        [
            l.set_visible(False)
            for (i, l) in enumerate(ax.get_xticklabels())
            if i % n != 0
        ]

    plt.title("Daily Chat Messages by Provider", pad=20, color="white")
    plt.xlabel("Date", color="white")
    plt.ylabel("Number of Messages", color="white")
    plt.tight_layout()
    plt.show()

    # save to file
    plt.savefig("daily_chat_messages.png")
