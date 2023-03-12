import pandas as pd
import yfinance as yf
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import plotly.graph_objects as go
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
import warnings
warnings.filterwarnings('ignore')
pd.options.display.float_format = '${:,.2f}'.format

hoy = datetime.today().strftime('%Y-%m-%d')

fecha_inicio = datetime.today() - relativedelta(years=10)

intc_df = yf.download("INTC", fecha_inicio, hoy)

intc_df.tail()

intc_df.reset_index(inplace=True)

intc_df.columns

# OUTPUT
# Index(['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], dtype='object')

df = intc_df[["Date", "Open"]]

df = intc_df[["Date", "Open"]]
nuevos_nombres = {
    "Date": "ds", 
    "Open": "y",
}

df.rename(columns=nuevos_nombres, inplace=True)


# precio de apertura
 
x = df["ds"]
y = df["y"]

figura = go.Figure()

figura.add_trace(go.Scatter(x=x, y=y))

figura.update_layout(
    title_text="Grafico de serie de la accion de su precio de apertura"
)

figura.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list(
                [
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all"),
                ]
            )
        ),
        rangeslider=dict(visible=True),
        type="date",
    )
)

figura.write_html("grafico.html")



m = Prophet(
    seasonality_mode="additive" 
)

m.fit(df)


futuro = m.make_future_dataframe(periods = 365)
futuro.tail()

prediccion = m.predict(futuro)
prediccion[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()


dia_siguiente = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')

prediccion[prediccion['ds'] == dia_siguiente]['yhat'].item()

plot_plotly(m, prediccion).write_html("prediccion.html")

plot_components_plotly(m, prediccion).write_html("compenentes_prediccion.html")