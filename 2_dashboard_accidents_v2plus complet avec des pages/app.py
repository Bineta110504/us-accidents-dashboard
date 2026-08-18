# ===========================================================
# app.py
# Point d'entrée de l'application. Assemble l'en-tête, le
# panneau de filtres global, le contenu de la page active
# (dash.page_container) et le pied de page. Le callback ici
# est le seul point qui écrit dans dcc.Store('filtres-store') ;
# chaque page ne fait que LIRE ce store.
# ===========================================================

import dash
from dash import Dash, html, Input, Output

from components.layout_commun import entete, panneau_filtres, pied_de_page

app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"],
)
app.title = "Dashboard Accidents"
server = app.server

app.layout = html.Div([
    entete(),
    panneau_filtres(),
    dash.page_container,
    pied_de_page(),
])


@app.callback(
    Output("filtres-store", "data"),
    Input("f-etat", "value"),
    Input("f-annee", "value"),
    Input("f-meteo", "value"),
    Input("f-jour", "value"),
    Input("f-route", "value"),
)
def maj_filtres(etat, annee, meteo, jour, route):
    return {"etat": etat, "annee": annee, "meteo": meteo, "jour": jour, "route": route}


if __name__ == "__main__":
    app.run(debug=True)
