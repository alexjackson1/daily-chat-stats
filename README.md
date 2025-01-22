# AI Chat Analytics

This Python script visualises your daily usage of OpenAI and Anthropic chat services by analysing your data export files. It creates a bar chart showing the number of messages you've sent each day to each provider.

## Prerequisites

- Python 3.6 or higher
- Required Python packages (install via `pip install -r requirements.txt`):
  - pandas
  - matplotlib
  - seaborn

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/alexjackson1/daily-chat-stats.git
   cd daily-chat-stats
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download your data exports:
   - OpenAI: Visit your account settings and request a data export
   - Anthropic: Visit your account settings and request a data export

4. Create the following directory structure in the repository:
   ```
   ai-chat-analytics/
   ├── main.py
   ├── requirements.txt
   ├── openai/
   └── anthropic/
   ```

5. Extract your downloaded data:
   - Place the OpenAI conversations.json file in the `openai` directory
   - Place the Anthropic conversations.json file in the `anthropic` directory

## Usage

Run the script from the command line:

```bash
python main.py
```

This will generate:
- A visualisation window showing your daily chat usage
- A saved image file `daily_chat_messages.png` in the current directory

## Output

The script generates a bar chart with:
- X-axis: Dates
- Y-axis: Number of messages sent
- Colour-coded bars for each provider (OpenAI in green, Anthropic in orange)
- Auto-scaling date labels for better readability

## Notes

- The script assumes your data export files are in the standard format provided by OpenAI and Anthropic as of January 2025
- Timestamps are converted to UTC for consistent comparison
- The visualisation uses a dark theme for better contrast

## Licence

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
