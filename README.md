

# Startup Dashboard

Welcome to the Startup Dashboard! This Streamlit application provides a comprehensive analysis of startup funding data. The app allows users to explore various metrics and visualizations related to startup investments, sectors, and investors.

Live at ![Dashboard}(https://startupfunding2010s.streamlit.app/)

## Features

- **Overall Analysis**: Get insights into total funding, maximum funding, average funding, and the number of funded startups. View month-on-month funding trends, top sectors, funding types, city-wise funding, top startups, and a funding heatmap.
- **Startup Analysis**: Analyze individual startups, including their industry, sub-industry, location, and funding rounds.
- **Investor Analysis**: Explore details about specific investors, including their recent investments, top investments, investment verticals, and round details. Additionally, view year-on-year investment trends for each investor.

## Installation

To run this application, you need to have Python and the required libraries installed. Follow these steps:

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install dependencies**:
    ```bash
    pip install streamlit numpy pandas matplotlib seaborn plotly
    ```

3. **Download the dataset**:
    Ensure that you have the dataset `startup_clean.csv` in the same directory as the script. The dataset should contain the following columns:
    - `startup`: Name of the startup
    - `amount`: Funding amount
    - `date`: Date of investment
    - `investors`: Names of investors
    - `vertical`: Industry sector
    - `subvertical`: Sub-industry sector
    - `city`: City of the startup
    - `round`: Funding round

## Usage

1. **Run the Streamlit application**:
    ```bash
    streamlit run app.py
    ```

2. **Interact with the Dashboard**:
    - **Sidebar**: Select the type of analysis you want to view (Overall Analysis, Startup, or Investors).
    - **Overall Analysis**: Click "Show Overall Analysis" to view metrics, trends, and charts related to the overall funding data.
    - **Startup Analysis**: Select a startup from the sidebar and click "Show Startup Analysis" to view detailed information about the selected startup.
    - **Investor Analysis**: Select an investor from the sidebar and click "Find Investor Details" to see insights about their investments.

## Features and Visualizations

- **Metrics**: Key statistics such as total funding, maximum funding, average funding, and number of funded startups.
- **Month-on-Month Funding Analysis**: Line chart showing funding trends over time.
- **Top Sectors**: Pie chart displaying the most funded sectors.
- **Funding Type Distribution**: Bar chart showing the distribution of different funding rounds.
- **City-wise Funding**: Bar chart representing funding amounts by city.
- **Top Startups**: Pie and bar charts showcasing the top startups by funding amount.
- **Funding Heatmap**: Heatmap showing the distribution of funding amounts across different years and funding rounds.
- **Startup Details**: Detailed view of a specific startup's industry, sub-industry, location, and funding rounds.
- **Investor Details**: Insights into an investor's recent investments, top investments, investment verticals, and round details, as well as year-on-year investment trends.

## Contributing

If you would like to contribute to this project, please follow these guidelines:

1. **Fork the repository** and create a new branch.
2. **Make your changes** and commit them with clear messages.
3. **Push your changes** to your forked repository.
4. **Create a pull request** with a description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [your-email@example.com](mailto:your-email@example.com).

---

Feel free to adjust any parts of the README to better fit your project specifics or preferences!
