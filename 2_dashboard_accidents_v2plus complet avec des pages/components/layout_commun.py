# ===========================================================
# components/layout_commun.py
# Éléments partagés par toutes les pages : en-tête, barre de
# navigation, panneau de filtres globaux et stockage des
# filtres (dcc.Store) partagé entre les pages.
# ===========================================================

import dash
from dash import html, dcc

from data_loader import LISTE_ETATS, LISTE_ANNEES, LISTE_METEO, COLONNES_CAUSES


def barre_navigation():
    liens = [
        html.Div(
            dcc.Link(f" {page['name']}", href=page["relative_path"], className="nav-link"),
            key=page["name"],
        )
        for page in dash.page_registry.values()
    ]
    return html.Nav(liens, className="nav-bar")


def entete():
    return html.Div([
        html.Div([
            html.H1("TABLEAU DE BORD DES ACCIDENTS", className="titre-principal"),
            html.P("Analyse interactive des accidents de la route aux États-Unis", className="sous-titre"),
        ]),
        barre_navigation(),
    ], className="header")


def panneau_filtres():
    """Panneau de filtres globaux, visible sur toutes les pages.
    Les valeurs sélectionnées sont écrites dans dcc.Store('filtres-store'),
    que chaque page lit ensuite en Input de ses propres callbacks."""
    return html.Div([
        html.Div([
            html.Label("État", className="filtre-label"),
            dcc.Dropdown(
                id="f-etat",
                options=[{"label": i, "value": i} for i in LISTE_ETATS],
                placeholder="Tous les états",
                className="filtre-dropdown",
            ),
        ], className="filtre-item"),

        html.Div([
            html.Label("Année", className="filtre-label"),
            dcc.Dropdown(
                id="f-annee",
                options=[{"label": str(i), "value": i} for i in LISTE_ANNEES],
                placeholder="Toutes les années",
                className="filtre-dropdown",
            ),
        ], className="filtre-item"),

        html.Div([
            html.Label("Météo", className="filtre-label"),
            dcc.Dropdown(
                id="f-meteo",
                options=[{"label": i, "value": i} for i in LISTE_METEO[:30]],
                placeholder="Toutes les conditions",
                className="filtre-dropdown",
            ),
        ], className="filtre-item"),

        html.Div([
            html.Label("Jour de la semaine", className="filtre-label"),
            dcc.Dropdown(
                id="f-jour",
                options=[
                    {"label": "Lundi", "value": "Monday"},
                    {"label": "Mardi", "value": "Tuesday"},
                    {"label": "Mercredi", "value": "Wednesday"},
                    {"label": "Jeudi", "value": "Thursday"},
                    {"label": "Vendredi", "value": "Friday"},
                    {"label": "Samedi", "value": "Saturday"},
                    {"label": "Dimanche", "value": "Sunday"},
                ],
                placeholder="Tous les jours",
                className="filtre-dropdown",
            ),
        ], className="filtre-item"),

        html.Div([
            html.Label("Type de route", className="filtre-label"),
            dcc.Dropdown(
                id="f-route",
                options=[{"label": v, "value": k} for k, v in COLONNES_CAUSES.items()],
                placeholder="Tous les types",
                className="filtre-dropdown",
            ),
        ], className="filtre-item"),

        dcc.Store(id="filtres-store"),
    ], className="filtres-avances")


def pied_de_page():
    return html.Footer([
        html.P("© 2026 - Bineta FAYE | Projet Final Dash | Tous droits réservés"),
        html.P("Données : US Accidents (Kaggle, sobhanmoosavi/us-accidents)", className="footer-sub"),
    ], className="footer")
