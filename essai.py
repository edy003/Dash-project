import dash
from dash import dcc, html
import plotly.graph_objects as go

# Initialisation de l'application
app = dash.Dash(__name__)

# Exemple de données
categories = [f"Catégorie {i}" for i in range(1, 12)]  # 11 éléments
valeurs = [i * 10 for i in range(1, 12)]

# Création du graphique à barres horizontales
fig = go.Figure(
    data=[
        go.Bar(
            x=valeurs,
            y=categories,
            orientation="h",
        )
    ]
)

# Mise à jour de la disposition
fig.update_layout(
    height=600,  # Hauteur totale du graphique
    margin=dict(l=10, r=10, t=30, b=10),  # Marges ajustées
    yaxis=dict(
        automargin=True,
        showgrid=False,
        showline=False,
    ),
)

# Mise en page de l'application
app.layout = html.Div(
    [
        html.H1("Graphique barh avec barre de défilement (en %)", style={"text-align": "center"}),
        html.Div(
            dcc.Graph(figure=fig),
            style={
                "height": "50%",  # Hauteur en pourcentage
                "overflowY": "auto",  # Barre de défilement verticale
                "border": "1px solid #ccc",  # Bordure pour visualisation
                "padding": "10px",
            },
        ),
    ],
    style={
        "height": "100vh",  # Hauteur du parent (fenêtre entière)
        "display": "flex",
        "flexDirection": "column",
    },
)

# Lancer l'application
if __name__ == "__main__":
    app.run_server(debug=True)
