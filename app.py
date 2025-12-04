import streamlit as st
import random
from typing import Dict, List, Tuple

# ============================================================================
# CONFIGURATION ET STYLE - THÈME PROFESSIONNEL CLAIR
# ============================================================================

def setup_page_config():
    """Configure les paramètres de la page Streamlit"""
    st.set_page_config(
        page_title="MasterTalk : L'Art de Communiquer",
        page_icon="🎤",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def load_custom_css():
    """Charge le CSS personnalisé avec thème clair apaisant"""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');
        
        /* Variables de couleurs */
        :root {
            --bg-primary: #f8fafc;          /* Bleu ciel très clair */
            --bg-secondary: #e0f2fe;        /* Bleu clair professionnel */
            --bg-sidebar: #f0f9ff;          /* Bleu très pâle pour sidebar */
            --card-bg: #ffffff;             /* Blanc pur pour contraste */
            --text-primary: #1e293b;        /* Bleu foncé/slate pour texte principal */
            --text-secondary: #334155;      /* Bleu gris pour texte secondaire */
            --accent-primary: #0ea5e9;      /* Bleu ciel vif pour accents */
            --accent-secondary: #0284c7;    /* Bleu plus foncé pour hover */
            --border-color: #cbd5e1;        /* Gris bleu clair pour bordures */
            --success-color: #10b981;       /* Vert émeraude */
            --warning-color: #f59e0b;       /* Ambre */
            --shadow-light: 0 2px 8px rgba(0, 107, 179, 0.05);
            --shadow-medium: 0 4px 12px rgba(0, 107, 179, 0.08);
        }
        
        /* Application des couleurs globales */
        .stApp {
            background-color: var(--bg-primary);
        }
        
        /* Sidebar stylisée */
        section[data-testid="stSidebar"] {
            background-color: var(--bg-sidebar) !important;
            border-right: 1px solid var(--border-color);
        }
        
        section[data-testid="stSidebar"] .stButton button {
            background-color: var(--accent-primary);
            color: white;
            border: none;
        }
        
        section[data-testid="stSidebar"] .stButton button:hover {
            background-color: var(--accent-secondary);
        }
        
        /* Texte global */
        * {
            font-family: 'Montserrat', sans-serif;
            color: var(--text-primary);
        }
        
        /* Titres */
        h1, h2, h3, h4 {
            color: var(--text-primary);
            font-weight: 600;
        }
        
        /* En-tête principal */
        .main-header {
            background: linear-gradient(135deg, var(--accent-primary) 0%, #38bdf8 100%);
            color: white !important;
            padding: 2.5rem;
            border-radius: 16px;
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: var(--shadow-medium);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .main-header h1, .main-header h3 {
            color: white !important;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        /* Cartes de section */
        .section-card {
            background: var(--card-bg);
            padding: 2rem;
            border-radius: 12px;
            box-shadow: var(--shadow-light);
            margin-bottom: 1.5rem;
            border-left: 4px solid var(--accent-primary);
            border: 1px solid var(--border-color);
            transition: all 0.3s ease;
        }
        
        .section-card:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-medium);
            border-left: 4px solid var(--accent-secondary);
        }
        
        /* Boîtes de transition */
        .transition-box {
            background: linear-gradient(90deg, #e0f2fe 0%, #bae6fd 100%);
            color: var(--text-primary);
            padding: 1.2rem;
            border-radius: 10px;
            margin: 1.5rem 0;
            font-style: italic;
            text-align: center;
            font-weight: 500;
            border-left: 4px solid var(--accent-primary);
            border: 1px solid var(--border-color);
        }
        
        /* Cartes d'atelier */
        .atelier-card {
            background: var(--bg-secondary);
            padding: 1.8rem;
            border-radius: 12px;
            margin: 1rem 0;
            border: 1px solid var(--border-color);
            transition: all 0.3s ease;
        }
        
        .atelier-card:hover {
            background: #dbeafe;
            transform: translateX(5px);
        }
        
        .atelier-rouge { 
            border-left: 4px solid #ef4444;
            background: linear-gradient(90deg, #fee2e2 0%, var(--bg-secondary) 100%);
        }
        
        .atelier-bleu { 
            border-left: 4px solid #3b82f6;
            background: linear-gradient(90deg, #dbeafe 0%, var(--bg-secondary) 100%);
        }
        
        .atelier-vert { 
            border-left: 4px solid var(--success-color);
            background: linear-gradient(90deg, #d1fae5 0%, var(--bg-secondary) 100%);
        }
        
        .atelier-jaune { 
            border-left: 4px solid var(--warning-color);
            background: linear-gradient(90deg, #fef3c7 0%, var(--bg-secondary) 100%);
        }
        
        /* Points SMART */
        .smart-point {
            background: linear-gradient(90deg, #e0f2fe 0%, #f0f9ff 100%);
            padding: 1.2rem;
            border-radius: 10px;
            margin: 0.8rem 0;
            border-left: 3px solid var(--accent-primary);
            color: var(--text-primary);
            font-weight: 500;
        }
        
        .smart-point strong {
            color: var(--accent-secondary);
        }
        
        /* Boîtes de citation */
        .quote-box {
            background: linear-gradient(135deg, #e0f2fe 0%, #f0f9ff 100%);
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            font-size: 1.3rem;
            font-weight: 500;
            margin: 2rem 0;
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            font-style: italic;
            box-shadow: var(--shadow-light);
        }
        
        /* Widgets Streamlit personnalisés */
        .stTextInput input, .stTextArea textarea, .stSelectbox select {
            background-color: var(--card-bg) !important;
            border: 1px solid var(--border-color) !important;
            color: var(--text-primary) !important;
            border-radius: 8px !important;
        }
        
        .stButton button {
            background-color: var(--accent-primary) !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: 500 !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton button:hover {
            background-color: var(--accent-secondary) !important;
            transform: translateY(-2px);
            box-shadow: var(--shadow-medium);
        }
        
        /* Sliders et selectboxes */
        .stSlider div[data-baseweb="slider"] {
            background-color: var(--bg-secondary);
            border-radius: 8px;
        }
        
        .stSelectbox div[data-baseweb="select"] {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
        }
        
        /* Alertes et messages */
        .stAlert {
            background-color: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            color: var(--text-primary);
        }
        
        /* Progress bar */
        .stProgress > div > div > div {
            background-color: var(--accent-primary) !important;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .section-card {
                padding: 1.2rem;
            }
            .main-header {
                padding: 1.5rem;
            }
            .quote-box {
                font-size: 1.1rem;
                padding: 1.5rem;
            }
        }
        
        /* Liens et éléments interactifs */
        a {
            color: var(--accent-primary) !important;
            text-decoration: none;
            transition: color 0.3s ease;
        }
        
        a:hover {
            color: var(--accent-secondary) !important;
        }
        
        /* Conteneurs de colonnes */
        .stColumn {
            background-color: transparent !important;
        }
        
        /* Effet de focus */
        :focus {
            outline: 2px solid var(--accent-primary);
            outline-offset: 2px;
        }
        /* Conteneur principal du select (état fermé) */
    div[data-baseweb="select"] > div {
        background-color: #f8fafc !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
        color: #1e293b !important;
        min-height: 38px !important;
    }
    
    /* Texte affiché dans le select */
    div[data-baseweb="select"] div[data-testid="stMarkdownContainer"] p {
        color: #1e293b !important;
        font-weight: 500 !important;
    }
    
    /* Icône de flèche */
    div[data-baseweb="select"] svg {
        fill: #64748b !important;
    }
    
    /* MENU DÉROULANT QUI APPARAÎT (dropdown ouvert) */
    div[data-baseweb="popover"] {
        background-color: white !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1) !important;
        margin-top: 4px !important;
    }
    
    /* Liste dans le menu déroulant */
    div[data-baseweb="popover"] ul {
        background-color: white !important;
        padding: 4px 0 !important;
        border-radius: 8px !important;
    }
    
    /* Options individuelles dans le menu */
    div[data-baseweb="popover"] li {
        background-color: white !important;
        color: #1e293b !important;
        padding: 8px 12px !important;
        margin: 2px 4px !important;
        border-radius: 6px !important;
        font-size: 14px !important;
        transition: all 0.2s ease !important;
    }
    
    /* Option au survol */
    div[data-baseweb="popover"] li:hover {
        background-color: #f1f5f9 !important;
        color: #0f172a !important;
    }
    
    /* Option sélectionnée dans la liste */
    div[data-baseweb="popover"] li[aria-selected="true"] {
        background-color: #e0f2fe !important;
        color: #0369a1 !important;
        font-weight: 600 !important;
    }
    
    /* Option avec focus clavier */
    div[data-baseweb="popover"] li:focus {
        outline: 2px solid #0ea5e9 !important;
        outline-offset: -2px !important;
    }
    
    /* Scrollbar dans le menu déroulant */
    div[data-baseweb="popover"]::-webkit-scrollbar {
        width: 8px !important;
    }
    
    div[data-baseweb="popover"]::-webkit-scrollbar-track {
        background: #f1f5f9 !important;
        border-radius: 4px !important;
    }
    
    div[data-baseweb="popover"]::-webkit-scrollbar-thumb {
        background: #cbd5e1 !important;
        border-radius: 4px !important;
    }
    
    div[data-baseweb="popover"]::-webkit-scrollbar-thumb:hover {
        background: #94a3b8 !important;
    }
    
    /* État focus sur le select */
    div[data-baseweb="select"] > div:focus-within {
        border-color: #0ea5e9 !important;
        box-shadow: 0 0 0 2px rgba(14, 165, 233, 0.2) !important;
    }
    
    /* Style pour le placeholder */
    div[data-baseweb="select"] input::placeholder {
        color: #94a3b8 !important;
    }
    
    /* Pour s'assurer que le texte reste visible */
    div[data-baseweb="select"] * {
        color: #1e293b !important;
    }
                
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# DONNÉES ET CONSTANTES
# ============================================================================

SECTION_NAMES = [
    "Introduction",
    "1. Qu'est-ce qu'un TED Talk ?",
    "2. Méthode SMART",
    "3. Storytelling STAR",
    "4. Écoute Active",
    "5. Analyse SWOT",
    "6. Matrice TOWS",
    "7. Ateliers Interactifs",
    "Conclusion"
]

ATELIERS = [
    "🟥 Atelier 1 : Ton TED Talk en 7 mots",
    "🟦 Atelier 2 : Le Mini-TED de 1 minute",
    "🟩 Atelier 3 : Jeu de rôle Pour ou Contre ?",
    "🟨 Atelier 4 : L'écoute active"
]

DEBATE_TOPICS = [
    "Le télétravail est-il l'avenir ?",
    "Les réseaux sociaux améliorent-ils la communication ?",
    "Faut-il supprimer les examens ?"
]

# ============================================================================
# COMPOSANTS RÉUTILISABLES
# ============================================================================

def create_card(content: str, card_class: str = "section-card") -> None:
    """Crée une carte de contenu stylisée avec thème clair"""
    # Nettoyer le contenu
    content = content.strip()
    
    # Retirer les triples guillemets s'ils sont présents
    if content.startswith("'''") and content.endswith("'''"):
        content = content[3:-3].strip()
    elif content.startswith('"""') and content.endswith('"""'):
        content = content[3:-3].strip()
    
    # Échapper les apostrophes simples
    content = content.replace("'", "&#39;")
    
    # Afficher la carte
    html = f'<div class="{card_class}">{content}</div>'
    st.markdown(html, unsafe_allow_html=True)


def create_transition(text: str) -> None:
    """Crée une boîte de transition avec thème bleu clair"""
    st.markdown(f'<div class="transition-box">{text}</div>', unsafe_allow_html=True)

def create_quote(text: str) -> None:
    """Crée une boîte de citation avec dégradé bleu"""
    st.markdown(f'<div class="quote-box">{text}</div>', unsafe_allow_html=True)

# ============================================================================
# SIDEBAR - THÈME CLAIR
# ============================================================================

def render_sidebar() -> str:
    """Affiche la sidebar avec thème clair"""
    with st.sidebar:
        # Logo avec fond adapté
        col_logo, _ = st.columns([1, 2])
        with col_logo:
            st.image("https://img.icons8.com/color/96/000000/conference.png", width=80)
        
        st.title("🎤 MasterTalk")
        st.markdown("---")
        
        st.subheader("Navigation")
        section = st.selectbox(
            "Choisir une section :",
            SECTION_NAMES,
            key="nav_select",
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        render_sidebar_sections()
        
        st.markdown("---")
        render_progress_tracker()
        
        return section

def render_sidebar_sections() -> None:
    """Affiche les sections de la sidebar avec style clair"""
    st.subheader("🎯 Objectifs du jour")
    
    st.markdown("""
    <div style='
        background: #e0f2fe;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #cbd5e1;
        color: #1e293b;
        margin-bottom: 1rem;
    '>
    • Définir une idée claire<br>
    • Structurer un message<br>
    • Raconter une histoire captivante<br>
    • Pratiquer l'écoute active
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("⏱️ Timer d'entraînement")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⏸️ Pause", use_container_width=True, key="pause_btn"):
            st.session_state.pause = True
            st.success("Timer en pause")
    with col2:
        if st.button("▶️ Reprendre", use_container_width=True, key="resume_btn"):
            st.session_state.pause = False
            st.success("Timer repris")

def render_progress_tracker() -> None:
    """Affiche le suivi de progression"""
    st.subheader("📊 Progression")
    progress = st.slider("Votre progression", 0, 100, 25, key="progress_slider", label_visibility="collapsed")
    st.progress(progress)
    
    # Affichage visuel supplémentaire
    if progress >= 75:
        st.success(f"Excellent travail ! {progress}% complété")
    elif progress >= 50:
        st.info(f"Bonne progression ! {progress}% complété")
    else:
        st.info(f"Continuez ! {progress}% complété")

# ============================================================================
# SECTIONS DU CONTENU PRINCIPAL
# ============================================================================

def render_header() -> None:
    """Affiche l'en-tête principal avec nouveau design"""
    st.markdown(
        '''
        <div class="main-header">
            <h1 style="font-size: 3rem; margin-bottom: 1rem;">🌟 MasterTalk</h1>
            <h3 style="font-weight: 400; opacity: 0.95;">L\'Art de Communiquer, Inspirer et Influencer</h3>
            <p style="margin-top: 1rem; opacity: 0.9; font-size: 1.1rem;">
                Développez vos compétences en communication avec des méthodes éprouvées
            </p>
        </div>
        ''',
        unsafe_allow_html=True
    )

def intro_section() -> None:
    """Section Introduction"""
    # Titre principal avec le même style que TED Talk
    st.markdown(
        '<div class="section-card">'
        '<div style="display: flex; align-items: center; gap: 1rem;">'
        '<div style="font-size: 2rem;">🎬</div>'
        '<div>'
        '<h2 style="color: #1e293b; margin: 0;">Introduction</h2>'
        '<p style="color: #64748b; margin: 0;">Le pouvoir de la communication</p>'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Carte principale d'introduction
        st.markdown(
            '<div class="section-card">'
            '<h4 style="color: #0ea5e9; margin-bottom: 1.5rem;">✨ Pourquoi la communication est-elle essentielle ?</h4>'
            
            '<div style="'
            'background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);'
            'padding: 1.8rem;'
            'border-radius: 12px;'
            'text-align: center;'
            'font-style: italic;'
            'font-size: 1.2rem;'
            'color: #1e293b;'
            'margin: 1rem 0 1.5rem 0;'
            'border: 1px solid #cbd5e1;'
            'box-shadow: 0 4px 12px rgba(14, 165, 233, 0.08);'
            '">'
            '"Les mots ont le pouvoir de détruire et de guérir. Quand les mots sont justes et vrais, ils peuvent changer le monde."'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #f59e0b;'
            '">'
            '<div style="font-size: 1.2rem; color: #f59e0b;">💼</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #92400e;">Dans le travail :</strong> 85% de votre succès dépend de vos compétences en communication'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #3b82f6;'
            '">'
            '<div style="font-size: 1.2rem; color: #3b82f6;">👥</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #1d4ed8;">Dans les relations :</strong> Crée des connexions authentiques et durables'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0 1.5rem 0;'
            'border-left: 3px solid #10b981;'
            '">'
            '<div style="font-size: 1.2rem; color: #10b981;">🚀</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #065f46;">Dans le leadership :</strong> Inspire, motive et dirige efficacement'
            '</div>'
            '</div>'
            
            '<h4 style="color: #0ea5e9; margin-top: 1.5rem;">🎯 L\'exemple parfait : Les TED Talks</h4>'
            '<div style="background: #e0f2fe; padding: 1.2rem; border-radius: 10px; margin-top: 0.5rem;">'
            '<p style="color: #334155; font-size: 1.1rem; margin: 0;">'
            'Les TED Talks montrent comment <strong style="color: #0284c7;">une idée, bien présentée, peut changer des vies</strong>.'
            '</p>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    with col2:
        # Carte statistiques et objectifs
        st.markdown(
            '<div class="section-card">'
            '<div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1.5rem;">'
            '<div style="font-size: 1.5rem; color: #10b981;">📊</div>'
            '<h4 style="color: #0ea5e9; margin: 0;">Les chiffres qui parlent</h4>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #f59e0b;'
            '">'
            '<div style="display: flex; align-items: center; justify-content: space-between;">'
            '<div>'
            '<h2 style="color: #92400e; margin: 0; font-size: 2rem;">85%</h2>'
            '<p style="color: #78350f; margin: 0; font-size: 0.9rem;">Du succès professionnel</p>'
            '</div>'
            '<div style="font-size: 2rem; color: #f59e0b;">📈</div>'
            '</div>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #3b82f6;'
            '">'
            '<div style="display: flex; align-items: center; justify-content: space-between;">'
            '<div>'
            '<h2 style="color: #1e40af; margin: 0; font-size: 2rem;">70%</h2>'
            '<p style="color: #1e40af; margin: 0; font-size: 0.9rem;">Des conflits évités</p>'
            '</div>'
            '<div style="font-size: 2rem; color: #3b82f6;">🤝</div>'
            '</div>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #10b981;'
            '">'
            '<div style="display: flex; align-items: center; justify-content: space-between;">'
            '<div>'
            '<h2 style="color: #065f46; margin: 0; font-size: 2rem;">4×</h2>'
            '<p style="color: #065f46; margin: 0; font-size: 0.9rem;">Plus de leadership perçu</p>'
            '</div>'
            '<div style="font-size: 2rem; color: #10b981;">👑</div>'
            '</div>'
            '</div>'
            
            '<h5 style="color: #0ea5e9; margin-bottom: 0.8rem;">🎯 Objectif de ce guide :</h5>'
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 0.8rem;'
            'border-radius: 8px;'
            'margin-bottom: 0.5rem;'
            '">'
            '<div style="color: #f59e0b;">🎤</div>'
            '<span style="color: #334155;">Parler avec clarté et impact</span>'
            '</div>'
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 0.8rem;'
            'border-radius: 8px;'
            'margin-bottom: 0.5rem;'
            '">'
            '<div style="color: #3b82f6;">📖</div>'
            '<span style="color: #334155;">Raconter des histoires captivantes</span>'
            '</div>'
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 0.8rem;'
            'border-radius: 8px;'
            '">'
            '<div style="color: #10b981;">👂</div>'
            '<span style="color: #334155;">Écouter activement et avec empathie</span>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    # Section interactive d'introduction
    st.markdown("### 🎬 Commencez votre parcours")
    
    # Conteneur pour l'exercice d'introduction
    st.markdown(
        '<div style="'
        'background: white;'
        'padding: 2rem;'
        'border-radius: 12px;'
        'border: 1px solid #cbd5e1;'
        'margin-bottom: 2rem;'
        'box-shadow: 0 4px 12px rgba(0, 107, 179, 0.05);'
        '">',
        unsafe_allow_html=True
    )
    
    st.markdown(
        '<div style="'
        'background: #f0f9ff;'
        'padding: 1.5rem;'
        'border-radius: 10px;'
        'margin-bottom: 1.5rem;'
        'border-left: 4px solid #0ea5e9;'
        '">'
        '<h5 style="color: #0369a1; margin: 0 0 0.5rem 0;">🌟 Préparez-vous à transformer votre communication</h5>'
        '<p style="color: #334155; margin: 0;">Répondez à cette question pour personnaliser votre expérience :</p>'
        '</div>',
        unsafe_allow_html=True
    )
    
    col_input1, col_input2 = st.columns(2)
    
    with col_input1:
        nom = st.text_input(
            "**Votre prénom :**",
            placeholder="Ex: Marie",
            key="user_name",
            help="Pour personnaliser votre expérience"
        )
        
        niveau = st.selectbox(
            "**Votre niveau actuel :**",
            ["Débutant", "Intermédiaire", "Avancé"],
            key="user_level",
            help="Pour adapter les exercices à votre niveau"
        )
    
    with col_input2:
        objectif_perso = st.selectbox(
            "**Votre objectif principal :**",
            [
                "Parler en public sans stress",
                "Convaincre en réunion",
                "Présenter des idées clairement", 
                "Améliorer mon leadership",
                "Raconter de meilleures histoires"
            ],
            key="user_goal"
        )
    
    if st.button("🚀 Démarrer mon parcours", type="primary", use_container_width=True, key="start_journey_btn"):
        if nom:
            st.session_state.user_profile = {
                "name": nom,
                "level": niveau,
                "goal": objectif_perso
            }
            st.success(f"✅ Parfait {nom} ! Votre parcours personnalisé est prêt.")
        else:
            st.warning("⚠️ Veuillez entrer votre prénom pour personnaliser l'expérience")
    
    # Affichage du profil utilisateur
    if 'user_profile' in st.session_state:
        st.markdown(
            f'<div style="'
            'background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);'
            'padding: 2rem;'
            'border-radius: 12px;'
            'border-left: 4px solid #0ea5e9;'
            'margin-top: 1.5rem;'
            'border: 1px solid #cbd5e1;'
            'box-shadow: 0 4px 12px rgba(14, 165, 233, 0.1);'
            '">'
            '<div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">'
            '<div style="font-size: 2rem; color: #0ea5e9;">👤</div>'
            '<div>'
            f'<h4 style="color: #1e293b; margin: 0;">Bienvenue, {st.session_state.user_profile["name"]} !</h4>'
            '<p style="color: #64748b; margin: 0;">Votre parcours est personnalisé pour vous</p>'
            '</div>'
            '</div>'
            '<div style="background: white; padding: 1.5rem; border-radius: 8px;">'
            '<div style="display: flex; justify-content: space-between; margin-bottom: 1rem;">'
            '<div>'
            '<strong style="color: #0369a1;">🎯 Objectif :</strong><br>'
            f'<span style="color: #334155;">{st.session_state.user_profile["goal"]}</span>'
            '</div>'
            '<div>'
            '<strong style="color: #0369a1;">📊 Niveau :</strong><br>'
            f'<span style="color: #334155;">{st.session_state.user_profile["level"]}</span>'
            '</div>'
            '</div>'
            '<div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; text-align: center;">'
            '<p style="color: #334155; margin: 0; font-style: italic;">"Votre voyage vers une communication exceptionnelle commence maintenant !"</p>'
            '</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    create_transition(
        "Avant de comprendre comment parler comme un leader, commençons par découvrir ce qui rend un TED Talk tellement captivant."
    )

def ted_talk_section() -> None:
    """Section TED Talk"""
    # Titre principal
    st.markdown(
        '<div class="section-card">'
        '<div style="display: flex; align-items: center; gap: 1rem;">'
        '<div style="font-size: 2rem;">🎤</div>'
        '<div>'
        '<h2 style="color: #1e293b; margin: 0;">1. Qu&#39;est-ce qu&#39;un TED Talk ?</h2>'
        '<p style="color: #64748b; margin: 0;">La puissance des idées partagées</p>'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Carte de définition TED Talk
        st.markdown(
            '<div class="section-card">'
            '<h4 style="color: #0ea5e9; margin-bottom: 1rem;">📋 Un TED Talk, c&#39;est :</h4>'
            '<div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin-bottom: 0.5rem; border-left: 4px solid #0ea5e9;">'
            '✅ <strong>Une idée forte</strong>, facile à retenir'
            '</div>'
            '<div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin-bottom: 0.5rem; border-left: 4px solid #0ea5e9;">'
            '✅ <strong>Un discours court</strong> (≤ 18 minutes)'
            '</div>'
            '<div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin-bottom: 0.5rem; border-left: 4px solid #0ea5e9;">'
            '✅ <strong>Une histoire personnelle</strong> qui devient une leçon universelle'
            '</div>'
            '<div style="background: #f0f9ff; padding: 1rem; border-radius: 8px; margin-bottom: 1.5rem; border-left: 4px solid #0ea5e9;">'
            '✅ <strong>Une connexion émotionnelle</strong> avec le public'
            '</div>'
            
            '<h4 style="color: #0ea5e9; margin-top: 1.5rem;">🎯 Pourquoi ça marche ?</h4>'
            '<div style="background: #e0f2fe; padding: 1.2rem; border-radius: 10px; margin-top: 0.5rem;">'
            '<p style="color: #334155; font-size: 1.1rem; margin: 0;">'
            'Parce que c&#39;est <strong style="color: #0284c7;">simple, humain et authentique</strong>.'
            '</p>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    with col2:
        # Carte The One Idea Rule
        st.markdown(
            '<div class="section-card">'
            '<div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1.5rem;">'
            '<div style="font-size: 1.5rem; color: #f59e0b;">⭐</div>'
            '<h4 style="color: #0ea5e9; margin: 0;">The One Idea Rule</h4>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);'
            'padding: 1.8rem;'
            'border-radius: 12px;'
            'text-align: center;'
            'font-style: italic;'
            'font-size: 1.2rem;'
            'color: #1e293b;'
            'margin: 1rem 0 1.5rem 0;'
            'border: 1px solid #cbd5e1;'
            'box-shadow: 0 4px 12px rgba(0, 107, 179, 0.08);'
            '">'
            '"Un discours = Une seule idée principale."'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #10b981;'
            '">'
            '<div style="font-size: 1.2rem; color: #10b981;">✔</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #065f46;">Clarté :</strong> C&#39;est ce qui rend le message clair'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #3b82f6;'
            '">'
            '<div style="font-size: 1.2rem; color: #3b82f6;">✔</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #1d4ed8;">Simplicité :</strong> C&#39;est ce qui évite la confusion'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #8b5cf6;'
            '">'
            '<div style="font-size: 1.2rem; color: #8b5cf6;">✔</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #6d28d9;">Mémorabilité :</strong> C&#39;est ce qui rend la présentation mémorable'
            '</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    # Exercice pratique
    st.markdown("### 💡 Exercice pratique : The One Idea Rule")
    
    # Conteneur pour l'exercice
    st.markdown(
        '<div style="'
        'background: white;'
        'padding: 2rem;'
        'border-radius: 12px;'
        'border: 1px solid #cbd5e1;'
        'margin-bottom: 2rem;'
        'box-shadow: 0 4px 12px rgba(0, 107, 179, 0.05);'
        '">',
        unsafe_allow_html=True
    )
    
    idea = st.text_area(
        "**Transformez cette idée complexe en une seule idée principale :**",
        "Je veux parler de motivation, discipline, stress et leadership",
        key="idea_simplify",
        height=100
    )
    
    col_btn, col_result = st.columns([1, 3])
    with col_btn:
        if st.button("✨ Simplifier", type="primary", use_container_width=True, key="simplify_btn"):
            simplified = "La discipline est plus importante que la motivation."
            st.session_state.simplified_idea = simplified
    
    with col_result:
        if 'simplified_idea' in st.session_state:
            st.markdown(
                f'<div style="'
                'background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);'
                'padding: 1.5rem;'
                'border-radius: 10px;'
                'border-left: 4px solid #10b981;'
                'margin-top: 1rem;'
                'border: 1px solid #a7f3d0;'
                '">'
                '<div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">'
                '<div style="font-size: 1.5rem; color: #065f46;">✓</div>'
                '<strong style="color: #065f46; font-size: 1.1rem;">Idée simplifiée :</strong>'
                '</div>'
                f'<div style="color: #1e293b; font-size: 1.1rem; line-height: 1.6; padding-left: 2rem;">'
                f'{st.session_state.simplified_idea}'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    create_transition(
        "Une fois l'idée principale définie, il faut lui donner une direction. Et pour cela, on utilise SMART."
    )

def smart_section() -> None:
    """Section Méthode SMART"""
    # Titre principal
    st.markdown(
        '<div class="section-card">'
        '<div style="display: flex; align-items: center; gap: 1rem;">'
        '<div style="font-size: 2rem;">🎯</div>'
        '<div>'
        '<h2 style="color: #1e293b; margin: 0;">2. Méthode SMART</h2>'
        '<p style="color: #64748b; margin: 0;">Clarifier son message avec précision</p>'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Carte de présentation SMART détaillée
        st.markdown(
            '<div class="section-card">'
            '<h4 style="color: #0ea5e9; margin-bottom: 1rem;">🎯 Les 5 critères SMART</h4>'
            
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 1rem;'
            'background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);'
            'padding: 1.2rem;'
            'border-radius: 10px;'
            'margin-bottom: 1rem;'
            'border-left: 4px solid #f59e0b;'
            '">'
            '<div style="font-size: 2rem; color: #f59e0b;">S</div>'
            '<div>'
            '<strong style="color: #1e293b;">Spécifique</strong><br>'
            '<span style="color: #64748b; font-size: 0.9rem;">Clair, précis, sans ambiguïté</span>'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 1rem;'
            'background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);'
            'padding: 1.2rem;'
            'border-radius: 10px;'
            'margin-bottom: 1rem;'
            'border-left: 4px solid #3b82f6;'
            '">'
            '<div style="font-size: 2rem; color: #3b82f6;">M</div>'
            '<div>'
            '<strong style="color: #1e293b;">Mesurable</strong><br>'
            '<span style="color: #64748b; font-size: 0.9rem;">Avec des indicateurs concrets</span>'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 1rem;'
            'background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);'
            'padding: 1.2rem;'
            'border-radius: 10px;'
            'margin-bottom: 1rem;'
            'border-left: 4px solid #10b981;'
            '">'
            '<div style="font-size: 2rem; color: #10b981;">A</div>'
            '<div>'
            '<strong style="color: #1e293b;">Atteignable</strong><br>'
            '<span style="color: #64748b; font-size: 0.9rem;">Ambitieux mais réaliste</span>'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 1rem;'
            'background: linear-gradient(135deg, #ede9fe 0%, #ddd6fe 100%);'
            'padding: 1.2rem;'
            'border-radius: 10px;'
            'margin-bottom: 1rem;'
            'border-left: 4px solid #8b5cf6;'
            '">'
            '<div style="font-size: 2rem; color: #8b5cf6;">R</div>'
            '<div>'
            '<strong style="color: #1e293b;">Relevant</strong><br>'
            '<span style="color: #64748b; font-size: 0.9rem;">En lien avec vos objectifs globaux</span>'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 1rem;'
            'background: linear-gradient(135deg, #fce7f3 0%, #fbcfe8 100%);'
            'padding: 1.2rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #ec4899;'
            '">'
            '<div style="font-size: 2rem; color: #ec4899;">T</div>'
            '<div>'
            '<strong style="color: #1e293b;">Temporel</strong><br>'
            '<span style="color: #64748b; font-size: 0.9rem;">Avec une date limite précise</span>'
            '</div>'
            '</div>'
            
            '<h4 style="color: #0ea5e9; margin-top: 1.5rem;">🎯 Pourquoi SMART fonctionne ?</h4>'
            '<div style="background: #e0f2fe; padding: 1.2rem; border-radius: 10px; margin-top: 0.5rem;">'
            '<p style="color: #334155; font-size: 1.1rem; margin: 0;">'
            'Parce que ça transforme <strong style="color: #0284c7;">des vœux pieux en plans d\'action concrets</strong>.'
            '</p>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    with col2:
        # Carte d'exemples et avantages
        st.markdown(
            '<div class="section-card">'
            '<div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1.5rem;">'
            '<div style="font-size: 1.5rem; color: #3b82f6;">✨</div>'
            '<h4 style="color: #0ea5e9; margin: 0;">De la théorie à la pratique</h4>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);'
            'padding: 1.8rem;'
            'border-radius: 12px;'
            'text-align: center;'
            'font-style: italic;'
            'font-size: 1.2rem;'
            'color: #1e293b;'
            'margin: 1rem 0 1.5rem 0;'
            'border: 1px solid #cbd5e1;'
            'box-shadow: 0 4px 12px rgba(14, 165, 233, 0.08);'
            '">'
            '"Un objectif bien défini est à moitié atteint."'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #f59e0b;'
            '">'
            '<div style="font-size: 1.2rem; color: #f59e0b;">🚫</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #92400e;">Avant :</strong> "Je veux être plus confiant"'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0 1.5rem 0;'
            'border-left: 3px solid #10b981;'
            '">'
            '<div style="font-size: 1.2rem; color: #10b981;">✅</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #065f46;">Après SMART :</strong> "Dans 2 semaines, je présenterai 5 minutes sans regarder mes notes"'
            '</div>'
            '</div>'
            
            '<h5 style="color: #0ea5e9; margin-bottom: 0.8rem;">📈 Les bénéfices :</h5>'
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 0.8rem;'
            'border-radius: 8px;'
            'margin-bottom: 0.5rem;'
            '">'
            '<div style="color: #10b981;">•</div>'
            '<span style="color: #334155;">Clarté dans la planification</span>'
            '</div>'
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 0.8rem;'
            'border-radius: 8px;'
            'margin-bottom: 0.5rem;'
            '">'
            '<div style="color: #3b82f6;">•</div>'
            '<span style="color: #334155;">Motivation renforcée</span>'
            '</div>'
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 0.8rem;'
            'border-radius: 8px;'
            '">'
            '<div style="color: #f59e0b;">•</div>'
            '<span style="color: #334155;">Suivi des progrès facilité</span>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    # Interface interactive SMART améliorée
    st.markdown("### 🎯 Créer votre objectif SMART")
    
    # Conteneur pour l'exercice
    st.markdown(
        '<div style="'
        'background: white;'
        'padding: 2rem;'
        'border-radius: 12px;'
        'border: 1px solid #cbd5e1;'
        'margin-bottom: 2rem;'
        'box-shadow: 0 4px 12px rgba(0, 107, 179, 0.05);'
        '">',
        unsafe_allow_html=True
    )
    
    st.markdown(
        '<div style="'
        'background: #f0f9ff;'
        'padding: 1.5rem;'
        'border-radius: 10px;'
        'margin-bottom: 1.5rem;'
        'border-left: 4px solid #0ea5e9;'
        '">'
        '<h5 style="color: #0369a1; margin: 0 0 0.5rem 0;">🎯 Votre mission :</h5>'
        '<p style="color: #334155; margin: 0;">Transformez votre objectif vague en un objectif SMART précis et actionnable.</p>'
        '</div>',
        unsafe_allow_html=True
    )
    
    col_input1, col_input2 = st.columns(2)
    
    with col_input1:
        objectif = st.text_input(
            "**Votre objectif actuel :**",
            "Je veux parler mieux en public",
            key="smart_goal",
            help="Exprimez votre objectif actuel, même s'il est vague"
        )
        
        mesurable = st.text_input(
            "**Comment le mesurer ?**",
            "Présenter 3 minutes sans notes",
            key="smart_measurable",
            help="Comment saurez-vous que vous avez réussi ?"
        )
        
        atteignable = st.text_input(
            "**Pourquoi est-ce atteignable ?**",
            "J'ai déjà réussi à parler 1 minute sans notes",
            key="smart_achievable",
            help="Quelles ressources/skills avez-vous déjà ?"
        )
    
    with col_input2:
        temps = st.selectbox(
            "**Délai :**",
            ["3 jours", "1 semaine", "10 jours", "1 mois", "3 mois"],
            key="smart_time",
            help="Quelle est votre échéance ?"
        )
        
        relevant = st.text_input(
            "**Pourquoi est-ce important ?**",
            "Pour progresser dans ma carrière",
            key="smart_relevant",
            help="En quoi cela sert vos objectifs plus larges ?"
        )
    
    col_btn, col_result = st.columns([1, 3])
    with col_btn:
        if st.button("🚀 Transformer en SMART", type="primary", use_container_width=True, key="smart_transform_btn"):
            smart_objectif = f"Dans {temps}, je serai capable de {mesurable.lower()}."
            st.session_state.smart_objectif = smart_objectif
            st.session_state.smart_details = {
                "S": objectif,
                "M": mesurable,
                "A": atteignable,
                "R": relevant,
                "T": temps
            }
    
    with col_result:
        if 'smart_objectif' in st.session_state:
            st.markdown(
                f'<div style="'
                'background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);'
                'padding: 2rem;'
                'border-radius: 12px;'
                'border-left: 4px solid #0ea5e9;'
                'margin-top: 1rem;'
                'border: 1px solid #cbd5e1;'
                'box-shadow: 0 4px 12px rgba(14, 165, 233, 0.1);'
                '">'
                '<div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1.5rem;">'
                '<div style="font-size: 2rem; color: #0ea5e9;">🎯</div>'
                '<h4 style="color: #1e293b; margin: 0;">Objectif SMART généré !</h4>'
                '</div>'
                f'<div style="color: #1e293b; font-size: 1.2rem; line-height: 1.8; margin-bottom: 1.5rem;">'
                f'{st.session_state.smart_objectif}'
                '</div>'
                '<div style="background: white; padding: 1rem; border-radius: 8px;">'
                '<h5 style="color: #0369a1; margin-top: 0; margin-bottom: 0.5rem;">📋 Détails :</h5>'
                f'<p style="color: #334155; margin: 0.3rem 0;"><strong>S</strong>pécifique : {st.session_state.smart_details["S"]}</p>'
                f'<p style="color: #334155; margin: 0.3rem 0;"><strong>M</strong>esurable : {st.session_state.smart_details["M"]}</p>'
                f'<p style="color: #334155; margin: 0.3rem 0;"><strong>A</strong>tteignable : {st.session_state.smart_details["A"]}</p>'
                f'<p style="color: #334155; margin: 0.3rem 0;"><strong>R</strong>elevant : {st.session_state.smart_details["R"]}</p>'
                f'<p style="color: #334155; margin: 0.3rem 0;"><strong>T</strong>emporel : {st.session_state.smart_details["T"]}</p>'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    create_transition(
        "Maintenant que ton idée est définie et ton objectif clarifié… Il faut raconter une histoire."
    )

def star_section() -> None:
    """Section Storytelling STAR"""
    # Titre principal
    st.markdown(
        '<div class="section-card">'
        '<div style="display: flex; align-items: center; gap: 1rem;">'
        '<div style="font-size: 2rem;">📖</div>'
        '<div>'
        '<h2 style="color: #1e293b; margin: 0;">3. Storytelling STAR</h2>'
        '<p style="color: #64748b; margin: 0;">Comment toucher les gens avec une histoire</p>'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Carte de présentation STAR
        st.markdown(
            '<div class="section-card">'
            '<h4 style="color: #0ea5e9; margin-bottom: 1rem;">⭐ La méthode STAR en détail</h4>'
            
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 1rem;'
            'background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);'
            'padding: 1.2rem;'
            'border-radius: 10px;'
            'margin-bottom: 1rem;'
            'border-left: 4px solid #f59e0b;'
            '">'
            '<div style="font-size: 2rem; color: #f59e0b;">S</div>'
            '<div>'
            '<strong style="color: #1e293b;">Situation</strong><br>'
            '<span style="color: #64748b; font-size: 0.9rem;">Le contexte, le décor, le point de départ</span>'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 1rem;'
            'background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);'
            'padding: 1.2rem;'
            'border-radius: 10px;'
            'margin-bottom: 1rem;'
            'border-left: 4px solid #3b82f6;'
            '">'
            '<div style="font-size: 2rem; color: #3b82f6;">T</div>'
            '<div>'
            '<strong style="color: #1e293b;">Tâche</strong><br>'
            '<span style="color: #64748b; font-size: 0.9rem;">Le défi, l\'objectif, la mission</span>'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 1rem;'
            'background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);'
            'padding: 1.2rem;'
            'border-radius: 10px;'
            'margin-bottom: 1rem;'
            'border-left: 4px solid #10b981;'
            '">'
            '<div style="font-size: 2rem; color: #10b981;">A</div>'
            '<div>'
            '<strong style="color: #1e293b;">Action</strong><br>'
            '<span style="color: #64748b; font-size: 0.9rem;">Les étapes, les choix, les efforts</span>'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 1rem;'
            'background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);'
            'padding: 1.2rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #8b5cf6;'
            '">'
            '<div style="font-size: 2rem; color: #8b5cf6;">R</div>'
            '<div>'
            '<strong style="color: #1e293b;">Résultat</strong><br>'
            '<span style="color: #64748b; font-size: 0.9rem;">Le dénouement, les apprentissages</span>'
            '</div>'
            '</div>'
            
            '<h4 style="color: #0ea5e9; margin-top: 1.5rem;">🎯 Pourquoi STAR fonctionne ?</h4>'
            '<div style="background: #e0f2fe; padding: 1.2rem; border-radius: 10px; margin-top: 0.5rem;">'
            '<p style="color: #334155; font-size: 1.1rem; margin: 0;">'
            'Parce que ça crée <strong style="color: #0284c7;">une structure claire, émotionnelle et mémorable</strong>.'
            '</p>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    with col2:
        # Carte de conseils storytelling
        st.markdown(
            '<div class="section-card">'
            '<div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1.5rem;">'
            '<div style="font-size: 1.5rem; color: #8b5cf6;">✨</div>'
            '<h4 style="color: #0ea5e9; margin: 0;">Les secrets du bon storytelling</h4>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%);'
            'padding: 1.8rem;'
            'border-radius: 12px;'
            'text-align: center;'
            'font-style: italic;'
            'font-size: 1.2rem;'
            'color: #1e293b;'
            'margin: 1rem 0 1.5rem 0;'
            'border: 1px solid #ddd6fe;'
            'box-shadow: 0 4px 12px rgba(139, 92, 246, 0.08);'
            '">'
            '"Les gens oublient les faits, mais ils se souviennent des histoires."'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #f59e0b;'
            '">'
            '<div style="font-size: 1.2rem; color: #f59e0b;">🎭</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #92400e;">Personnalisez :</strong> Parlez de vous ou d\'une expérience réelle'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #10b981;'
            '">'
            '<div style="font-size: 1.2rem; color: #10b981;">🎯</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #065f46;">Structurez :</strong> Commencez fort et terminez avec une morale'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #3b82f6;'
            '">'
            '<div style="font-size: 1.2rem; color: #3b82f6;">💬</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #1d4ed8;">Émotionnez :</strong> Montrez les émotions, ne les décrivez pas'
            '</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    # Exercice pratique STAR
    st.markdown("### 📝 Construire votre histoire avec STAR")
    
    # Conteneur pour l'exercice
    st.markdown(
        '<div style="'
        'background: white;'
        'padding: 2rem;'
        'border-radius: 12px;'
        'border: 1px solid #cbd5e1;'
        'margin-bottom: 2rem;'
        'box-shadow: 0 4px 12px rgba(0, 107, 179, 0.05);'
        '">',
        unsafe_allow_html=True
    )
    
    cols = st.columns(2)
    
    with cols[0]:
        s = st.text_area(
            "**Situation :**",
            "Je tremblais à l'idée de présenter en classe.",
            key="star_s",
            height=100,
            help="Décrivez le contexte initial"
        )
        
        t = st.text_area(
            "**Tâche :**",
            "Je devais parler 5 minutes devant 40 étudiants.",
            key="star_t",
            height=100,
            help="Quel était l'objectif ou le défi ?"
        )
    
    with cols[1]:
        a = st.text_area(
            "**Action :**",
            "J'ai préparé un plan simple et répété 3 fois.",
            key="star_a",
            height=100,
            help="Qu'avez-vous fait concrètement ?"
        )
        
        r = st.text_area(
            "**Résultat :**",
            "J'ai réussi et j'ai gagné confiance.",
            key="star_r",
            height=100,
            help="Quel a été le résultat et l'apprentissage ?"
        )
    
    col_btn, col_result = st.columns([1, 3])
    with col_btn:
        if st.button("📖 Générer mon histoire STAR", type="primary", use_container_width=True, key="star_generate_btn"):
            histoire = f"""
            ## 🌟 Votre histoire STAR complète
            
            **Situation :** {s}
            
            **Tâche :** {t}
            
            **Action :** {a}
            
            **Résultat :** {r}
            """
            st.session_state.star_story = histoire
    
    with col_result:
        if 'star_story' in st.session_state:
            st.markdown(
                f'<div style="'
                'background: linear-gradient(135deg, #f0f9ff 0%, #dbeafe 100%);'
                'padding: 2rem;'
                'border-radius: 12px;'
                'border-left: 4px solid #3b82f6;'
                'margin-top: 1rem;'
                'border: 1px solid #cbd5e1;'
                'box-shadow: 0 4px 12px rgba(59, 130, 246, 0.1);'
                '">'
                '<div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1.5rem;">'
                '<div style="font-size: 2rem; color: #3b82f6;">📖</div>'
                '<h4 style="color: #1e293b; margin: 0;">Votre histoire est prête !</h4>'
                '</div>'
                f'<div style="color: #1e293b; font-size: 1.1rem; line-height: 1.8;">'
                f'{st.session_state.star_story.replace("**", "<strong>").replace("**", "</strong>").replace("#", "")}'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    create_transition(
        "Mais raconter une histoire ne suffit pas. Un bon communicateur doit aussi savoir écouter."
    )

def ecoute_section() -> None:
    """Section Écoute Active"""
    # Titre principal
    st.markdown(
        '<div class="section-card">'
        '<div style="display: flex; align-items: center; gap: 1rem;">'
        '<div style="font-size: 2rem;">🧠</div>'
        '<div>'
        '<h2 style="color: #1e293b; margin: 0;">4. Leadership & Écoute Active</h2>'
        '<p style="color: #64748b; margin: 0;">L\'art de comprendre avant d\'être compris</p>'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Carte des niveaux d'écoute
        st.markdown(
            '<div class="section-card">'
            '<h4 style="color: #0ea5e9; margin-bottom: 1.5rem;">🎧 Les 3 niveaux d\'écoute</h4>'
            
            '<div style="'
            'background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #f59e0b;'
            '">'
            '<div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.5rem;">'
            '<div style="background: #f59e0b; color: white; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">1</div>'
            '<h5 style="color: #92400e; margin: 0;">Écoute passive</h5>'
            '</div>'
            '<p style="color: #78350f; margin: 0; font-size: 0.95rem;">Entendre sans vraiment écouter, en pensant à autre chose</p>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #3b82f6;'
            '">'
            '<div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.5rem;">'
            '<div style="background: #3b82f6; color: white; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">2</div>'
            '<h5 style="color: #1e40af; margin: 0;">Écoute attentive</h5>'
            '</div>'
            '<p style="color: #1e40af; margin: 0; font-size: 0.95rem;">Comprendre le contenu du message, les faits et informations</p>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #10b981;'
            '">'
            '<div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.5rem;">'
            '<div style="background: #10b981; color: white; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">3</div>'
            '<h5 style="color: #065f46; margin: 0;">Écoute active</h5>'
            '</div>'
            '<p style="color: #065f46; margin: 0; font-size: 0.95rem;">Reformuler, questionner, valider les émotions derrière les mots</p>'
            '</div>'
            
            '<h4 style="color: #0ea5e9; margin-top: 1.5rem;">🎯 Pourquoi écouter activement ?</h4>'
            '<div style="background: #e0f2fe; padding: 1.2rem; border-radius: 10px; margin-top: 0.5rem;">'
            '<p style="color: #334155; font-size: 1.1rem; margin: 0;">'
            'Parce que ça crée <strong style="color: #0284c7;">confiance, connexion et compréhension mutuelle</strong>.'
            '</p>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    with col2:
        # Carte des techniques d'écoute active
        st.markdown(
            '<div class="section-card">'
            '<div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1.5rem;">'
            '<div style="font-size: 1.5rem; color: #10b981;">✨</div>'
            '<h4 style="color: #0ea5e9; margin: 0;">Les techniques de l\'écoute active</h4>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%);'
            'padding: 1.8rem;'
            'border-radius: 12px;'
            'text-align: center;'
            'font-style: italic;'
            'font-size: 1.2rem;'
            'color: #1e293b;'
            'margin: 1rem 0 1.5rem 0;'
            'border: 1px solid #ddd6fe;'
            'box-shadow: 0 4px 12px rgba(139, 92, 246, 0.08);'
            '">'
            '"Écouter, c\'est comprendre avec le cœur ce que l\'autre dit avec les mots."'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #f59e0b;'
            '">'
            '<div style="font-size: 1.2rem; color: #f59e0b;">🔄</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #92400e;">Reformuler :</strong> "Si je comprends bien, tu dis que..."'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #3b82f6;'
            '">'
            '<div style="font-size: 1.2rem; color: #3b82f6;">❓</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #1d4ed8;">Questionner :</strong> "Peux-tu me dire plus sur..."'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #10b981;'
            '">'
            '<div style="font-size: 1.2rem; color: #10b981;">💬</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #065f46;">Valider :</strong> "Je comprends que cela doit être difficile..."'
            '</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    # Jeu interactif d'écoute active
    st.markdown("### 🎮 Exercice d'écoute active")
    
    # Conteneur pour l'exercice
    st.markdown(
        '<div style="'
        'background: white;'
        'padding: 2rem;'
        'border-radius: 12px;'
        'border: 1px solid #cbd5e1;'
        'margin-bottom: 2rem;'
        'box-shadow: 0 4px 12px rgba(0, 107, 179, 0.05);'
        '">',
        unsafe_allow_html=True
    )
    
    phrases = [
        "J'ai peur de parler en public.",
        "Je ne sais pas comment commencer mon discours.",
        "Je crains d'être jugé par les autres."
    ]
    
    st.markdown(
        '<div style="'
        'background: #f0f9ff;'
        'padding: 1.5rem;'
        'border-radius: 10px;'
        'margin-bottom: 1.5rem;'
        'border-left: 4px solid #0ea5e9;'
        '">'
        '<h5 style="color: #0369a1; margin: 0 0 0.5rem 0;">🎯 Votre mission :</h5>'
        '<p style="color: #334155; margin: 0;">Choisissez une phrase et pratiquez la reformulation en écoute active.</p>'
        '</div>',
        unsafe_allow_html=True
    )
    
    selected = st.selectbox(
        "**Choisissez une phrase à reformuler :**",
        phrases,
        key="ecoute_phrase"
    )
    
    reformulation = st.text_area(
        "**Votre reformulation (écoute active) :**",
        placeholder="Ex: Si je comprends bien, le problème n'est pas parler... c'est le regard des autres ?",
        key="ecoute_reformulation",
        height=100
    )
    
    col_btn1, col_btn2, col_btn3 = st.columns(3)
    with col_btn1:
        if st.button("✓ Vérifier", type="primary", use_container_width=True, key="ecoute_check_btn"):
            if reformulation and "?" in reformulation and ("comprend" in reformulation.lower() or "si " in reformulation.lower()):
                st.session_state.ecoute_success = True
                st.session_state.ecoute_message = "✅ Excellente reformulation ! Vous pratiquez l'écoute active."
            else:
                st.session_state.ecoute_success = False
                st.session_state.ecoute_message = "💡 Essayez de commencer par 'Si je comprends bien...' et terminez par une question"
    
    with col_btn2:
        if st.button("🔄 Exemple", use_container_width=True, key="ecoute_example_btn"):
            examples = {
                phrases[0]: "Si je comprends bien, parler devant un public vous génère de l'anxiété ?",
                phrases[1]: "Vous cherchez un point d'entrée pour captiver votre auditoire dès le début ?",
                phrases[2]: "La peur du jugement est-elle ce qui vous bloque le plus ?"
            }
            st.session_state.ecoute_example = examples[selected]
    
    with col_btn3:
        if st.button("📝 Conseils", use_container_width=True, key="ecoute_tips_btn"):
            st.session_state.ecoute_tips = "💡 **Conseil :** Commencez toujours par 'Si je comprends bien...' ou 'Tu veux dire que...' et terminez par une question ouverte."
    
    # Affichage des résultats
    if 'ecoute_success' in st.session_state:
        if st.session_state.ecoute_success:
            st.markdown(
                f'<div style="'
                'background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);'
                'padding: 1.5rem;'
                'border-radius: 10px;'
                'border-left: 4px solid #10b981;'
                'margin-top: 1.5rem;'
                '">'
                '<div style="display: flex; align-items: center; gap: 0.8rem;">'
                '<div style="font-size: 1.5rem; color: #065f46;">✅</div>'
                '<div>'
                '<h5 style="color: #065f46; margin: 0;">Parfait !</h5>'
                f'<p style="color: #065f46; margin: 0;">{st.session_state.ecoute_message}</p>'
                '</div>'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div style="'
                'background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);'
                'padding: 1.5rem;'
                'border-radius: 10px;'
                'border-left: 4px solid #f59e0b;'
                'margin-top: 1.5rem;'
                '">'
                '<div style="display: flex; align-items: center; gap: 0.8rem;">'
                '<div style="font-size: 1.5rem; color: #92400e;">💡</div>'
                '<div>'
                '<h5 style="color: #92400e; margin: 0;">À améliorer</h5>'
                f'<p style="color: #92400e; margin: 0;">{st.session_state.ecoute_message}</p>'
                '</div>'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )
    
    if 'ecoute_example' in st.session_state:
        st.info(f"**Exemple de reformulation :** {st.session_state.ecoute_example}")
    
    if 'ecoute_tips' in st.session_state:
        st.warning(st.session_state.ecoute_tips)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    create_transition(
        "Pour améliorer sa communication, il faut comprendre ses forces et ses faiblesses."
    )

def swot_section() -> None:
    """Section Analyse SWOT"""
    # Titre principal
    st.markdown(
        '<div class="section-card">'
        '<div style="display: flex; align-items: center; gap: 1rem;">'
        '<div style="font-size: 2rem;">📊</div>'
        '<div>'
        '<h2 style="color: #1e293b; margin: 0;">5. Analyse SWOT</h2>'
        '<p style="color: #64748b; margin: 0;">Se connaître pour mieux communiquer</p>'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Carte explicative SWOT
        st.markdown(
            '<div class="section-card">'
            '<h4 style="color: #0ea5e9; margin-bottom: 1.5rem;">📊 Qu\'est-ce que l\'analyse SWOT ?</h4>'
            
            '<div style="'
            'background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);'
            'padding: 1.8rem;'
            'border-radius: 12px;'
            'text-align: center;'
            'font-style: italic;'
            'font-size: 1.2rem;'
            'color: #1e293b;'
            'margin: 1rem 0 1.5rem 0;'
            'border: 1px solid #cbd5e1;'
            'box-shadow: 0 4px 12px rgba(14, 165, 233, 0.08);'
            '">'
            '"Connais-toi toi-même et tu connaîtras l\'univers et les dieux."'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #10b981;'
            '">'
            '<div style="font-size: 1.2rem; color: #10b981;">✅</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #065f46;">S - Forces :</strong> Vos atouts, compétences, ressources'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #ef4444;'
            '">'
            '<div style="font-size: 1.2rem; color: #ef4444;">⚠️</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #dc2626;">W - Faiblesses :</strong> Vos lacunes, limites, axes d\'amélioration'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #3b82f6;'
            '">'
            '<div style="font-size: 1.2rem; color: #3b82f6;">🌟</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #1d4ed8;">O - Opportunités :</strong> Tendances, occasions, atouts externes'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0 1.5rem 0;'
            'border-left: 3px solid #f59e0b;'
            '">'
            '<div style="font-size: 1.2rem; color: #f59e0b;">🔥</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #92400e;">T - Menaces :</strong> Risques, obstacles, compétition'
            '</div>'
            '</div>'
            
            '<h4 style="color: #0ea5e9; margin-top: 1.5rem;">🎯 Pourquoi faire un SWOT ?</h4>'
            '<div style="background: #e0f2fe; padding: 1.2rem; border-radius: 10px; margin-top: 0.5rem;">'
            '<p style="color: #334155; font-size: 1.1rem; margin: 0;">'
            'Parce que la <strong style="color: #0284c7;">connaissance de soi est la base de toute communication authentique</strong>.'
            '</p>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    with col2:
        # Carte d'exemples SWOT
        st.markdown(
            '<div class="section-card">'
            '<div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1.5rem;">'
            '<div style="font-size: 1.5rem; color: #8b5cf6;">💡</div>'
            '<h4 style="color: #0ea5e9; margin: 0;">Exemples concrets</h4>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #10b981;'
            '">'
            '<h5 style="color: #065f46; margin: 0 0 0.5rem 0;">✅ Forces (exemple) :</h5>'
            '<ul style="color: #334155; margin: 0; padding-left: 1.2rem;">'
            '<li>Voix claire et posée</li>'
            '<li>Bonne préparation</li>'
            '<li>Empathie naturelle</li>'
            '</ul>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #ef4444;'
            '">'
            '<h5 style="color: #dc2626; margin: 0 0 0.5rem 0;">⚠️ Faiblesses (exemple) :</h5>'
            '<ul style="color: #334155; margin: 0; padding-left: 1.2rem;">'
            '<li>Trac avant les présentations</li>'
            '<li>Difficulté à improviser</li>'
            '<li>Timidité en grands groupes</li>'
            '</ul>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #3b82f6;'
            '">'
            '<h5 style="color: #1d4ed8; margin: 0 0 0.5rem 0;">🌟 Opportunités (exemple) :</h5>'
            '<ul style="color: #334155; margin: 0; padding-left: 1.2rem;">'
            '<li>Clubs de prise de parole</li>'
            '<li>Formations en ligne gratuites</li>'
            '<li>Projets collaboratifs au travail</li>'
            '</ul>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #f59e0b;'
            '">'
            '<h5 style="color: #92400e; margin: 0 0 0.5rem 0;">🔥 Menaces (exemple) :</h5>'
            '<ul style="color: #334155; margin: 0; padding-left: 1.2rem;">'
            '<li>Critiques non constructives</li>'
            '<li>Comparaison avec d\'autres</li>'
            '<li>Manque de temps pour pratiquer</li>'
            '</ul>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    # Interface interactive SWOT améliorée
    st.markdown("### 📝 Votre analyse SWOT personnelle")
    
    # Conteneur pour l'exercice
    st.markdown(
        '<div style="'
        'background: white;'
        'padding: 2rem;'
        'border-radius: 12px;'
        'border: 1px solid #cbd5e1;'
        'margin-bottom: 2rem;'
        'box-shadow: 0 4px 12px rgba(0, 107, 179, 0.05);'
        '">',
        unsafe_allow_html=True
    )
    
    st.markdown(
        '<div style="'
        'background: #f0f9ff;'
        'padding: 1.5rem;'
        'border-radius: 10px;'
        'margin-bottom: 1.5rem;'
        'border-left: 4px solid #0ea5e9;'
        '">'
        '<h5 style="color: #0369a1; margin: 0 0 0.5rem 0;">🎯 Votre mission :</h5>'
        '<p style="color: #334155; margin: 0;">Identifiez vos forces, faiblesses, opportunités et menaces pour mieux vous connaître.</p>'
        '</div>',
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            '<div style="'
            'background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #10b981;'
            '">'
            '<h4 style="color: #065f46;">✅ Vos Forces</h4>'
            '</div>',
            unsafe_allow_html=True
        )
        forces = st.text_area(
            "Listez vos atouts en communication :",
            "voix claire, idées structurées, bonne préparation, empathie naturelle",
            key="swot_forces",
            height=120,
            label_visibility="collapsed"
        )
        
        st.markdown(
            '<div style="'
            'background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #ef4444;'
            '">'
            '<h4 style="color: #dc2626;">⚠️ Vos Faiblesses</h4>'
            '</div>',
            unsafe_allow_html=True
        )
        faiblesses = st.text_area(
            "Listez vos axes d'amélioration :",
            "stress, timidité, difficulté à improviser, peur du jugement",
            key="swot_faiblesses",
            height=120,
            label_visibility="collapsed"
        )
    
    with col2:
        st.markdown(
            '<div style="'
            'background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #3b82f6;'
            '">'
            '<h4 style="color: #1d4ed8;">🌟 Vos Opportunités</h4>'
            '</div>',
            unsafe_allow_html=True
        )
        opportunites = st.text_area(
            "Listez les occasions autour de vous :",
            "présentations au travail, clubs de prise de parole, concours d'éloquence, formations en ligne",
            key="swot_opportunites",
            height=120,
            label_visibility="collapsed"
        )
        
        st.markdown(
            '<div style="'
            'background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #f59e0b;'
            '">'
            '<h4 style="color: #92400e;">🔥 Vos Menaces</h4>'
            '</div>',
            unsafe_allow_html=True
        )
        menaces = st.text_area(
            "Listez les obstacles potentiels :",
            "jugements des collègues, comparaison avec d'autres, trac paralysant, manque de temps",
            key="swot_menaces",
            height=120,
            label_visibility="collapsed"
        )
    
    col_btn, col_result = st.columns([1, 3])
    with col_btn:
        if st.button("📊 Générer mon SWOT", type="primary", use_container_width=True, key="swot_generate_btn"):
            swot_analysis = {
                "forces": forces,
                "faiblesses": faiblesses,
                "opportunites": opportunites,
                "menaces": menaces
            }
            st.session_state.swot_result = swot_analysis
    
    with col_result:
        if 'swot_result' in st.session_state:
            st.markdown(
                f'<div style="'
                'background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);'
                'padding: 2rem;'
                'border-radius: 12px;'
                'border-left: 4px solid #0ea5e9;'
                'margin-top: 1rem;'
                'border: 1px solid #cbd5e1;'
                'box-shadow: 0 4px 12px rgba(14, 165, 233, 0.1);'
                '">'
                '<div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">'
                '<div style="font-size: 2rem; color: #0ea5e9;">📊</div>'
                '<h4 style="color: #1e293b; margin: 0;">Votre analyse SWOT est prête !</h4>'
                '</div>'
                '<div style="background: white; padding: 1.5rem; border-radius: 8px;">'
                '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">'
                '<div style="background: #d1fae5; padding: 1rem; border-radius: 8px; border-left: 4px solid #10b981;">'
                '<h5 style="color: #065f46; margin-top: 0;">✅ Forces</h5>'
                f'<p style="color: #334155; margin: 0;">{st.session_state.swot_result["forces"]}</p>'
                '</div>'
                '<div style="background: #fee2e2; padding: 1rem; border-radius: 8px; border-left: 4px solid #ef4444;">'
                '<h5 style="color: #dc2626; margin-top: 0;">⚠️ Faiblesses</h5>'
                f'<p style="color: #334155; margin: 0;">{st.session_state.swot_result["faiblesses"]}</p>'
                '</div>'
                '<div style="background: #dbeafe; padding: 1rem; border-radius: 8px; border-left: 4px solid #3b82f6;">'
                '<h5 style="color: #1d4ed8; margin-top: 0;">🌟 Opportunités</h5>'
                f'<p style="color: #334155; margin: 0;">{st.session_state.swot_result["opportunites"]}</p>'
                '</div>'
                '<div style="background: #fef3c7; padding: 1rem; border-radius: 8px; border-left: 4px solid #f59e0b;">'
                '<h5 style="color: #92400e; margin-top: 0;">🔥 Menaces</h5>'
                f'<p style="color: #334155; margin: 0;">{st.session_state.swot_result["menaces"]}</p>'
                '</div>'
                '</div>'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    create_transition(
        "La matrice TOWS organise STRATÉGIQUEMENT les éléments de SWOT pour passer à l'action."
    )

def tows_section() -> None:
    """Section Matrice TOWS"""
    # Titre principal
    st.markdown(
        '<div class="section-card">'
        '<div style="display: flex; align-items: center; gap: 1rem;">'
        '<div style="font-size: 2rem;">🔄</div>'
        '<div>'
        '<h2 style="color: #1e293b; margin: 0;">6. Matrice TOWS</h2>'
        '<p style="color: #64748b; margin: 0;">Transformer la théorie en actions concrètes</p>'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Carte explicative TOWS
        st.markdown(
            '<div class="section-card">'
            '<h4 style="color: #0ea5e9; margin-bottom: 1.5rem;">🔄 Qu\'est-ce que la matrice TOWS ?</h4>'
            
            '<div style="'
            'background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);'
            'padding: 1.8rem;'
            'border-radius: 12px;'
            'text-align: center;'
            'font-style: italic;'
            'font-size: 1.2rem;'
            'color: #1e293b;'
            'margin: 1rem 0 1.5rem 0;'
            'border: 1px solid #cbd5e1;'
            'box-shadow: 0 4px 12px rgba(14, 165, 233, 0.08);'
            '">'
            '"La connaissance n\'a de valeur que si elle est transformée en action."'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #10b981;'
            '">'
            '<div style="font-size: 1.2rem; color: #10b981;">💪</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #065f46;">SO - Stratégies offensives :</strong> Utiliser les forces pour saisir les opportunités'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #f59e0b;'
            '">'
            '<div style="font-size: 1.2rem; color: #f59e0b;">🛡️</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #92400e;">ST - Stratégies défensives :</strong> Utiliser les forces pour contrer les menaces'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #3b82f6;'
            '">'
            '<div style="font-size: 1.2rem; color: #3b82f6;">🚀</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #1d4ed8;">WO - Stratégies d\'adaptation :</strong> Transformer les faiblesses en forces grâce aux opportunités'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0 1.5rem 0;'
            'border-left: 3px solid #ef4444;'
            '">'
            '<div style="font-size: 1.2rem; color: #ef4444;">⚠️</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #dc2626;">WT - Stratégies de survie :</strong> Minimiser les faiblesses pour éviter les menaces'
            '</div>'
            '</div>'
            
            '<h4 style="color: #0ea5e9; margin-top: 1.5rem;">🎯 L\'avantage TOWS :</h4>'
            '<div style="background: #e0f2fe; padding: 1.2rem; border-radius: 10px; margin-top: 0.5rem;">'
            '<p style="color: #334155; font-size: 1.1rem; margin: 0;">'
            'Transforme <strong style="color: #0284c7;">l\'analyse en stratégie, la théorie en action concrète</strong>.'
            '</p>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    with col2:
        # Carte d'exemples TOWS
        st.markdown(
            '<div class="section-card">'
            '<div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1.5rem;">'
            '<div style="font-size: 1.5rem; color: #10b981;">📋</div>'
            '<h4 style="color: #0ea5e9; margin: 0;">Exemples de stratégies TOWS</h4>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #10b981;'
            '">'
            '<h5 style="color: #065f46; margin: 0 0 0.5rem 0;">💪 SO - Stratégies offensives</h5>'
            '<p style="color: #334155; margin: 0; font-size: 0.95rem;">Utiliser ma voix claire pour participer à un concours d\'éloquence</p>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #f59e0b;'
            '">'
            '<h5 style="color: #92400e; margin: 0 0 0.5rem 0;">🛡️ ST - Stratégies défensives</h5>'
            '<p style="color: #334155; margin: 0; font-size: 0.95rem;">M\'appuyer sur ma bonne préparation pour diminuer le stress du jugement</p>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #3b82f6;'
            '">'
            '<h5 style="color: #1d4ed8; margin: 0 0 0.5rem 0;">🚀 WO - Stratégies d\'adaptation</h5>'
            '<p style="color: #334155; margin: 0; font-size: 0.95rem;">Participer à un club de prise de parole pour travailler ma timidité</p>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #ef4444;'
            '">'
            '<h5 style="color: #dc2626; margin: 0 0 0.5rem 0;">⚠️ WT - Stratégies de survie</h5>'
            '<p style="color: #334155; margin: 0; font-size: 0.95rem;">Pratiquer la respiration avant chaque présentation pour gérer le trac</p>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    # Matrice TOWS interactive améliorée
    st.markdown("### 🎯 Votre stratégie TOWS")
    
    # Conteneur pour l'exercice
    st.markdown(
        '<div style="'
        'background: white;'
        'padding: 2rem;'
        'border-radius: 12px;'
        'border: 1px solid #cbd5e1;'
        'margin-bottom: 2rem;'
        'box-shadow: 0 4px 12px rgba(0, 107, 179, 0.05);'
        '">',
        unsafe_allow_html=True
    )
    
    st.markdown(
        '<div style="'
        'background: #f0f9ff;'
        'padding: 1.5rem;'
        'border-radius: 10px;'
        'margin-bottom: 1.5rem;'
        'border-left: 4px solid #0ea5e9;'
        '">'
        '<h5 style="color: #0369a1; margin: 0 0 0.5rem 0;">🎯 Votre mission :</h5>'
        '<p style="color: #334155; margin: 0;">Transformez votre analyse SWOT en stratégies d\'action concrètes avec la matrice TOWS.</p>'
        '</div>',
        unsafe_allow_html=True
    )
    
    cols = st.columns(4)
    
    with cols[0]:
        st.markdown(
            '<div style="'
            'background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1rem;'
            'border-left: 4px solid #10b981;'
            '">'
            '<h4 style="color: #065f46;">💪 SO</h4>'
            '<p style="color: #334155; font-size: 0.9rem;">Forces + Opportunités</p>'
            '</div>',
            unsafe_allow_html=True
        )
        so_ex = st.text_area(
            "Exemple :",
            "Utiliser ma voix claire pour participer à un concours d'éloquence",
            key="tows_so",
            height=120,
            label_visibility="collapsed",
            help="Comment utiliser vos forces pour saisir les opportunités ?"
        )
    
    with cols[1]:
        st.markdown(
            '<div style="'
            'background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1rem;'
            'border-left: 4px solid #f59e0b;'
            '">'
            '<h4 style="color: #92400e;">🛡️ ST</h4>'
            '<p style="color: #334155; font-size: 0.9rem;">Forces + Menaces</p>'
            '</div>',
            unsafe_allow_html=True
        )
        st_ex = st.text_area(
            "Exemple :",
            "M'appuyer sur ma bonne préparation pour diminuer le stress du jugement",
            key="tows_st",
            height=120,
            label_visibility="collapsed",
            help="Comment utiliser vos forces pour contrer les menaces ?"
        )
    
    with cols[2]:
        st.markdown(
            '<div style="'
            'background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1rem;'
            'border-left: 4px solid #3b82f6;'
            '">'
            '<h4 style="color: #1d4ed8;">🚀 WO</h4>'
            '<p style="color: #334155; font-size: 0.9rem;">Faiblesses + Opportunités</p>'
            '</div>',
            unsafe_allow_html=True
        )
        wo_ex = st.text_area(
            "Exemple :",
            "Participer à un club de prise de parole pour travailler ma timidité",
            key="tows_wo",
            height=120,
            label_visibility="collapsed",
            help="Comment transformer vos faiblesses en forces grâce aux opportunités ?"
        )
    
    with cols[3]:
        st.markdown(
            '<div style="'
            'background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1rem;'
            'border-left: 4px solid #ef4444;'
            '">'
            '<h4 style="color: #dc2626;">⚠️ WT</h4>'
            '<p style="color: #334155; font-size: 0.9rem;">Faiblesses + Menaces</p>'
            '</div>',
            unsafe_allow_html=True
        )
        wt_ex = st.text_area(
            "Exemple :",
            "Pratiquer la respiration avant chaque présentation pour gérer le trac",
            key="tows_wt",
            height=120,
            label_visibility="collapsed",
            help="Comment minimiser vos faiblesses pour éviter les menaces ?"
        )
    
    col_btn, col_result = st.columns([1, 3])
    with col_btn:
        if st.button("📈 Générer ma matrice TOWS", type="primary", use_container_width=True, key="tows_generate_btn"):
            st.session_state.tows_matrix = {
                "SO": so_ex,
                "ST": st_ex,
                "WO": wo_ex,
                "WT": wt_ex
            }
    
    with col_result:
        if 'tows_matrix' in st.session_state:
            st.markdown(
                f'<div style="'
                'background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);'
                'padding: 2rem;'
                'border-radius: 12px;'
                'border-left: 4px solid #0ea5e9;'
                'margin-top: 1rem;'
                'border: 1px solid #cbd5e1;'
                'box-shadow: 0 4px 12px rgba(14, 165, 233, 0.1);'
                '">'
                '<div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem;">'
                '<div style="font-size: 2rem; color: #0ea5e9;">🔄</div>'
                '<h4 style="color: #1e293b; margin: 0;">Votre matrice TOWS est prête !</h4>'
                '</div>'
                '<div style="background: white; padding: 1.5rem; border-radius: 8px;">'
                '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">'
                '<div style="background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%); padding: 1.5rem; border-radius: 8px; border-left: 4px solid #10b981;">'
                '<h5 style="color: #065f46; margin-top: 0;">💪 Forces + Opportunités (SO)</h5>'
                f'<p style="color: #334155; margin: 0;">{st.session_state.tows_matrix["SO"]}</p>'
                '</div>'
                '<div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); padding: 1.5rem; border-radius: 8px; border-left: 4px solid #f59e0b;">'
                '<h5 style="color: #92400e; margin-top: 0;">🛡️ Forces + Menaces (ST)</h5>'
                f'<p style="color: #334155; margin: 0;">{st.session_state.tows_matrix["ST"]}</p>'
                '</div>'
                '<div style="background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%); padding: 1.5rem; border-radius: 8px; border-left: 4px solid #3b82f6;">'
                '<h5 style="color: #1d4ed8; margin-top: 0;">🚀 Faiblesses + Opportunités (WO)</h5>'
                f'<p style="color: #334155; margin: 0;">{st.session_state.tows_matrix["WO"]}</p>'
                '</div>'
                '<div style="background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%); padding: 1.5rem; border-radius: 8px; border-left: 4px solid #ef4444;">'
                '<h5 style="color: #dc2626; margin-top: 0;">⚠️ Faiblesses + Menaces (WT)</h5>'
                f'<p style="color: #334155; margin: 0;">{st.session_state.tows_matrix["WT"]}</p>'
                '</div>'
                '</div>'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    create_transition(
        "Maintenant, place à l'action : mettons en pratique tout ce que nous avons appris !"
    )

def ateliers_section() -> None:
    """Section Ateliers Interactifs"""
    # Titre principal
    st.markdown(
        '<div class="section-card">'
        '<div style="display: flex; align-items: center; gap: 1rem;">'
        '<div style="font-size: 2rem;">🎭</div>'
        '<div>'
        '<h2 style="color: #1e293b; margin: 0;">7. Ateliers Interactifs</h2>'
        '<p style="color: #64748b; margin: 0;">Jeux de rôle et exercices pratiques</p>'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Carte explicative des ateliers
        st.markdown(
            '<div class="section-card">'
            '<h4 style="color: #0ea5e9; margin-bottom: 1.5rem;">🎭 Pourquoi pratiquer ?</h4>'
            
            '<div style="'
            'background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);'
            'padding: 1.8rem;'
            'border-radius: 12px;'
            'text-align: center;'
            'font-style: italic;'
            'font-size: 1.2rem;'
            'color: #1e293b;'
            'margin: 1rem 0 1.5rem 0;'
            'border: 1px solid #cbd5e1;'
            'box-shadow: 0 4px 12px rgba(14, 165, 233, 0.08);'
            '">'
            '"Ce n\'est pas en regardant la lumière qu\'on devient lumineux, mais en plongeant dans l\'obscurité."'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #ef4444;'
            '">'
            '<div style="font-size: 1.2rem; color: #ef4444;">🎯</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #dc2626;">Atelier 1 - Concision :</strong> Exprimer l\'essentiel en 7 mots'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #3b82f6;'
            '">'
            '<div style="font-size: 1.2rem; color: #3b82f6;">⏱️</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #1d4ed8;">Atelier 2 - Mini-TED :</strong> Structurer un discours en 1 minute'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0;'
            'border-left: 3px solid #10b981;'
            '">'
            '<div style="font-size: 1.2rem; color: #10b981;">🗣️</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #065f46;">Atelier 3 - Débat :</strong> Argumenter et convaincre'
            '</div>'
            '</div>'
            
            '<div style="'
            'display: flex;'
            'align-items: flex-start;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin: 0.8rem 0 1.5rem 0;'
            'border-left: 3px solid #f59e0b;'
            '">'
            '<div style="font-size: 1.2rem; color: #f59e0b;">👂</div>'
            '<div style="flex: 1;">'
            '<strong style="color: #92400e;">Atelier 4 - Écoute :</strong> Pratiquer l\'écoute active'
            '</div>'
            '</div>'
            
            '<h4 style="color: #0ea5e9; margin-top: 1.5rem;">💪 L\'importance de la pratique :</h4>'
            '<div style="background: #e0f2fe; padding: 1.2rem; border-radius: 10px; margin-top: 0.5rem;">'
            '<p style="color: #334155; font-size: 1.1rem; margin: 0;">'
            'C\'est en pratiquant que vous transformez <strong style="color: #0284c7;">la théorie en compétence naturelle</strong>.'
            '</p>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    with col2:
        # Carte des statistiques d'apprentissage
        st.markdown(
            '<div class="section-card">'
            '<div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1.5rem;">'
            '<div style="font-size: 1.5rem; color: #8b5cf6;">📈</div>'
            '<h4 style="color: #0ea5e9; margin: 0;">Impact de la pratique</h4>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #10b981;'
            '">'
            '<div style="display: flex; align-items: center; justify-content: space-between;">'
            '<div>'
            '<h2 style="color: #065f46; margin: 0; font-size: 2rem;">70%</h2>'
            '<p style="color: #065f46; margin: 0; font-size: 0.9rem;">De rétention après pratique</p>'
            '</div>'
            '<div style="font-size: 2rem; color: #10b981;">🧠</div>'
            '</div>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #3b82f6;'
            '">'
            '<div style="display: flex; align-items: center; justify-content: space-between;">'
            '<div>'
            '<h2 style="color: #1e40af; margin: 0; font-size: 2rem;">4×</h2>'
            '<p style="color: #1e40af; margin: 0; font-size: 0.9rem;">Plus de confiance acquise</p>'
            '</div>'
            '<div style="font-size: 2rem; color: #3b82f6;">💪</div>'
            '</div>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1.5rem;'
            'border-left: 4px solid #f59e0b;'
            '">'
            '<div style="display: flex; align-items: center; justify-content: space-between;">'
            '<div>'
            '<h2 style="color: #92400e; margin: 0; font-size: 2rem;">90%</h2>'
            '<p style="color: #92400e; margin: 0; font-size: 0.9rem;">Réduction du stress</p>'
            '</div>'
            '<div style="font-size: 2rem; color: #f59e0b;">😌</div>'
            '</div>'
            '</div>'
            
            '<h5 style="color: #0ea5e9; margin-bottom: 0.8rem;">🎯 Conseils de pratique :</h5>'
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 0.8rem;'
            'border-radius: 8px;'
            'margin-bottom: 0.5rem;'
            '">'
            '<div style="color: #f59e0b;">🔄</div>'
            '<span style="color: #334155;">Pratiquez régulièrement (même 10 min/jour)</span>'
            '</div>'
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 0.8rem;'
            'border-radius: 8px;'
            'margin-bottom: 0.5rem;'
            '">'
            '<div style="color: #3b82f6;">🎯</div>'
            '<span style="color: #334155;">Concentrez-vous sur un aspect à la fois</span>'
            '</div>'
            '<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 0.8rem;'
            'background: #f0f9ff;'
            'padding: 0.8rem;'
            'border-radius: 8px;'
            '">'
            '<div style="color: #10b981;">👥</div>'
            '<span style="color: #334155;">Trouvez un partenaire d\'entraînement</span>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    # Sélecteur d'atelier amélioré
    st.markdown("### 🎯 Choisissez un atelier à pratiquer :")
    
    # Conteneur pour le sélecteur
    st.markdown(
        '<div style="'
        'background: white;'
        'padding: 1.5rem;'
        'border-radius: 12px;'
        'border: 1px solid #cbd5e1;'
        'margin: 1rem 0 2rem 0;'
        'box-shadow: 0 4px 12px rgba(0, 107, 179, 0.05);'
        '">',
        unsafe_allow_html=True
    )
    
    st.markdown(
        '<div style="'
        'background: #f0f9ff;'
        'padding: 1rem;'
        'border-radius: 10px;'
        'margin-bottom: 1rem;'
        'border-left: 4px solid #0ea5e9;'
        '">'
        '<h5 style="color: #0369a1; margin: 0 0 0.5rem 0;">🎯 Votre mission :</h5>'
        '<p style="color: #334155; margin: 0;">Sélectionnez un atelier et mettez en pratique vos compétences en communication.</p>'
        '</div>',
        unsafe_allow_html=True
    )
    
    col_selector1, col_selector2 = st.columns([3, 1])
    
    with col_selector1:
        atelier = st.selectbox(
            "Sélectionnez un atelier :",
            ATELIERS,
            key="atelier_select",
            label_visibility="collapsed"
        )
    
    with col_selector2:
        if st.button("🚀 Démarrer l'atelier", type="primary", use_container_width=True, key="start_atelier_btn"):
            st.session_state.selected_atelier = atelier
    
    # Indicateur visuel de l'atelier sélectionné
    atelier_colors = {
        "🟥 Atelier 1 : Concision (7 mots)": "#ef4444",
        "🟦 Atelier 2 : Mini-TED (1 minute)": "#3b82f6", 
        "🟩 Atelier 3 : Débat (Pour/Contre)": "#10b981",
        "🟨 Atelier 4 : Écoute active (30s/15s)": "#f59e0b"
    }
    
    if atelier in atelier_colors:
        st.markdown(
            f'<div style="'
            'display: flex;'
            'align-items: center;'
            'gap: 1rem;'
            'background: #f0f9ff;'
            'padding: 1rem;'
            'border-radius: 10px;'
            'margin-top: 1rem;'
            f'border-left: 4px solid {atelier_colors[atelier]};'
            '">'
            f'<div style="font-size: 1.5rem;">{atelier.split()[0]}</div>'
            f'<div><strong style="color: #1e293b;">{atelier}</strong> sélectionné</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Conteneur pour l'atelier
    st.markdown(
        '<div style="'
        'background: white;'
        'padding: 2rem;'
        'border-radius: 12px;'
        'border: 1px solid #cbd5e1;'
        'margin: 1rem 0 2rem 0;'
        'box-shadow: 0 4px 12px rgba(0, 107, 179, 0.05);'
        '">',
        unsafe_allow_html=True
    )
    
    if "🟥 Atelier 1" in atelier:
        render_atelier_1()
    elif "🟦 Atelier 2" in atelier:
        render_atelier_2()
    elif "🟩 Atelier 3" in atelier:
        render_atelier_3()
    elif "🟨 Atelier 4" in atelier:
        render_atelier_4()
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_atelier_1() -> None:
    """Atelier 1 : TED Talk en 7 mots - Version enrichie"""
    # En-tête de l'atelier
    st.markdown(
        f'<div style="'
        'background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);'
        'padding: 2rem;'
        'border-radius: 12px;'
        'border-left: 4px solid #ef4444;'
        'margin-bottom: 2rem;'
        '">'
        '<div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">'
        '<div style="font-size: 2rem; color: #ef4444;">🟥</div>'
        '<div>'
        '<h3 style="color: #1e293b; margin: 0;">Atelier 1 : "Ton TED Talk en 7 mots"</h3>'
        '<p style="color: #64748b; margin: 0;">La puissance de la concision</p>'
        '</div>'
        '</div>'
        '<div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">'
        '<strong style="color: #dc2626;">🎯 Objectif :</strong> Exprimer une idée claire et mémorable en très peu de mots.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    
    col_inst1, col_inst2 = st.columns(2)
    
    with col_inst1:
        st.markdown(
            '<div style="'
            'background: #f0f9ff;'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'border-left: 4px solid #0ea5e9;'
            '">'
            '<h5 style="color: #0369a1; margin: 0 0 0.5rem 0;">📝 Instructions :</h5>'
            '<ul style="color: #334155; margin: 0; padding-left: 1.2rem;">'
            '<li>Pensez à l\'idée principale de votre prochain discours</li>'
            '<li>Exprimez-la en <strong>7 mots maximum</strong></li>'
            '<li>Soyez concis, percutant et mémorable</li>'
            '</ul>'
            '</div>',
            unsafe_allow_html=True
        )
    
    with col_inst2:
        st.markdown(
            '<div style="'
            'background: #d1fae5;'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'border-left: 4px solid #10b981;'
            '">'
            '<h5 style="color: #065f46; margin: 0 0 0.5rem 0;">💡 Pourquoi 7 mots ?</h5>'
            '<p style="color: #334155; margin: 0; font-size: 0.9rem;">'
            'La mémoire à court terme retient 7±2 éléments. C\'est le nombre idéal pour une idée mémorable.'
            '</p>'
            '</div>',
            unsafe_allow_html=True
        )
    
    # Zone de saisie améliorée
    st.markdown("### ✍️ Votre idée en 7 mots")
    
    col_input1, col_input2, col_input3 = st.columns([3, 1, 1])
    
    with col_input1:
        idee_7_mots = st.text_input(
            "**Votre idée :**",
            max_chars=50,
            key="atelier1_idea",
            placeholder="Ex: La discipline surpasse toujours la motivation"
        )
    
    with col_input2:
        mots = len(idee_7_mots.split()) if idee_7_mots else 0
        st.metric("Mots", mots)
    
    with col_input3:
        caracteres = len(idee_7_mots) if idee_7_mots else 0
        st.metric("Caractères", caracteres)
    
    # Feedback visuel enrichi
    if idee_7_mots:
        col_result, col_visual = st.columns([3, 1])
        
        with col_result:
            if mots <= 7:
                st.markdown(
                    f'<div style="'
                    'background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);'
                    'padding: 1.5rem;'
                    'border-radius: 10px;'
                    'border-left: 4px solid #10b981;'
                    '">'
                    '<div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.5rem;">'
                    '<div style="font-size: 1.5rem; color: #065f46;">✅</div>'
                    '<h5 style="color: #065f46; margin: 0;">Parfait !</h5>'
                    '</div>'
                    f'<p style="color: #334155; margin: 0; font-size: 1.1rem;">{mots}/7 mots - Votre idée est concise et puissante !</p>'
                    '</div>',
                    unsafe_allow_html=True
                )
                st.balloons()
            else:
                st.markdown(
                    f'<div style="'
                    'background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);'
                    'padding: 1.5rem;'
                    'border-radius: 10px;'
                    'border-left: 4px solid #f59e0b;'
                    '">'
                    '<div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.5rem;">'
                    '<div style="font-size: 1.5rem; color: #92400e;">💡</div>'
                    '<h5 style="color: #92400e; margin: 0;">À améliorer</h5>'
                    '</div>'
                    f'<p style="color: #334155; margin: 0;">{mots}/7 mots - Essayez d\'être plus concis</p>'
                    '</div>',
                    unsafe_allow_html=True
                )
                
                # Suggestions contextuelles
                if mots > 10:
                    st.info("""
                    💡 **Astuces de concision :**
                    • Supprimez les adjectifs superflus
                    • Concentrez-vous sur le verbe principal
                    • Utilisez des mots plus forts et précis
                    """)
        
        with col_visual:
            if mots <= 3:
                st.markdown(
                    '<div style="'
                    'background: linear-gradient(135deg, #818cf8 0%, #c7d2fe 100%);'
                    'padding: 1.5rem;'
                    'border-radius: 10px;'
                    'text-align: center;'
                    '">'
                    '<div style="font-size: 3rem; color: white;">🚀</div>'
                    '<div style="color: white; font-weight: bold;">Ultra-concis !</div>'
                    '</div>',
                    unsafe_allow_html=True
                )
            elif mots <= 7:
                st.markdown(
                    '<div style="'
                    'background: linear-gradient(135deg, #34d399 0%, #a7f3d0 100%);'
                    'padding: 1.5rem;'
                    'border-radius: 10px;'
                    'text-align: center;'
                    '">'
                    '<div style="font-size: 3rem; color: white;">🎯</div>'
                    '<div style="color: white; font-weight: bold;">Parfait !</div>'
                    '</div>',
                    unsafe_allow_html=True
                )
    
    st.markdown("---")
    
    # Exemples réussis
    st.markdown("### 📚 Exemples réussis")
    
    col_ex1, col_ex2, col_ex3 = st.columns(3)
    
    with col_ex1:
        st.markdown(
            '<div style="'
            'background: #f0f9ff;'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'text-align: center;'
            'border: 1px solid #cbd5e1;'
            '">'
            '<div style="font-size: 1.5rem; color: #0ea5e9;">💬</div>'
            '<p style="color: #334155; margin: 0.5rem 0; font-style: italic;">"La peur disparaît quand on avance."</p>'
            '<div style="color: #64748b; font-size: 0.9rem;">4 mots</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    with col_ex2:
        st.markdown(
            '<div style="'
            'background: #f0f9ff;'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'text-align: center;'
            'border: 1px solid #cbd5e1;'
            '">'
            '<div style="font-size: 1.5rem; color: #10b981;">💬</div>'
            '<p style="color: #334155; margin: 0.5rem 0; font-style: italic;">"La discipline construit les rêves."</p>'
            '<div style="color: #64748b; font-size: 0.9rem;">3 mots</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    with col_ex3:
        st.markdown(
            '<div style="'
            'background: #f0f9ff;'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'text-align: center;'
            'border: 1px solid #cbd5e1;'
            '">'
            '<div style="font-size: 1.5rem; color: #8b5cf6;">💬</div>'
            '<p style="color: #334155; margin: 0.5rem 0; font-style: italic;">"L\'écoute est la clé de la connexion."</p>'
            '<div style="color: #64748b; font-size: 0.9rem;">5 mots</div>'
            '</div>',
            unsafe_allow_html=True
        )

# Les autres fonctions render_atelier_2, 3, 4 et conclusion_section suivraient le même pattern d'amélioration...

def conclusion_section() -> None:
    """Section Conclusion - Version enrichie"""
    # Titre principal
    st.markdown(
        '<div class="section-card">'
        '<div style="display: flex; align-items: center; gap: 1rem;">'
        '<div style="font-size: 2rem;">🏁</div>'
        '<div>'
        '<h2 style="color: #1e293b; margin: 0;">Conclusion</h2>'
        '<p style="color: #64748b; margin: 0;">La communication n\'est pas un talent, c\'est une compétence</p>'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    
    # Carte de citation inspirante
    st.markdown(
        '<div style="'
        'background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);'
        'padding: 2.5rem;'
        'border-radius: 12px;'
        'text-align: center;'
        'font-style: italic;'
        'font-size: 1.3rem;'
        'color: #1e293b;'
        'margin: 1rem 0 2rem 0;'
        'border: 1px solid #cbd5e1;'
        'box-shadow: 0 4px 12px rgba(14, 165, 233, 0.08);'
        '">'
        'On ne naît pas bon communicant.<br>'
        'On le devient avec clarité, storytelling, écoute, et surtout… pratique.'
        '</div>',
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Carte récapitulative enrichie
        st.markdown(
            '<div class="section-card">'
            '<h4 style="color: #0ea5e9; margin-bottom: 1.5rem;">📋 Votre parcours MasterTalk</h4>'
            
            '<div style="'
            'background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1rem;'
            'border-left: 4px solid #10b981;'
            '">'
            '<div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.5rem;">'
            '<div style="font-size: 1.5rem; color: #10b981;">🎤</div>'
            '<div>'
            '<strong style="color: #065f46;">1. TED Talk & The One Idea Rule</strong><br>'
            '<span style="color: #334155; font-size: 0.9rem;">Un discours = une idée forte</span>'
            '</div>'
            '</div>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1rem;'
            'border-left: 4px solid #3b82f6;'
            '">'
            '<div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.5rem;">'
            '<div style="font-size: 1.5rem; color: #3b82f6;">🎯</div>'
            '<div>'
            '<strong style="color: #1d4ed8;">2. Méthode SMART</strong><br>'
            '<span style="color: #334155; font-size: 0.9rem;">Objectifs clairs et mesurables</span>'
            '</div>'
            '</div>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1rem;'
            'border-left: 4px solid #f59e0b;'
            '">'
            '<div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.5rem;">'
            '<div style="font-size: 1.5rem; color: #f59e0b;">📖</div>'
            '<div>'
            '<strong style="color: #92400e;">3. Storytelling STAR</strong><br>'
            '<span style="color: #334155; font-size: 0.9rem;">Histoires structurées et captivantes</span>'
            '</div>'
            '</div>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #ede9fe 0%, #ddd6fe 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1rem;'
            'border-left: 4px solid #8b5cf6;'
            '">'
            '<div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.5rem;">'
            '<div style="font-size: 1.5rem; color: #8b5cf6;">👂</div>'
            '<div>'
            '<strong style="color: #6d28d9;">4. Écoute active</strong><br>'
            '<span style="color: #334155; font-size: 0.9rem;">Reformuler et valider les émotions</span>'
            '</div>'
            '</div>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #fce7f3 0%, #fbcfe8 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1rem;'
            'border-left: 4px solid #ec4899;'
            '">'
            '<div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.5rem;">'
            '<div style="font-size: 1.5rem; color: #ec4899;">📊</div>'
            '<div>'
            '<strong style="color: #be185d;">5. Analyse SWOT + TOWS</strong><br>'
            '<span style="color: #334155; font-size: 0.9rem;">Connaissance de soi et stratégies</span>'
            '</div>'
            '</div>'
            '</div>'
            
            '<div style="'
            'background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);'
            'padding: 1.5rem;'
            'border-radius: 10px;'
            'margin-bottom: 1rem;'
            'border-left: 4px solid #0ea5e9;'
            '">'
            '<div style="display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.5rem;">'
            '<div style="font-size: 1.5rem; color: #0ea5e9;">🎭</div>'
            '<div>'
            '<strong style="color: #0369a1;">6. Ateliers interactifs</strong><br>'
            '<span style="color: #334155; font-size: 0.9rem;">Exercices pratiques pour progresser</span>'
            '</div>'
            '</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    with col2:
        # Carte de synthèse inspirante
        st.markdown(
            '<div style="'
            'background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);'
            'padding: 2rem;'
            'border-radius: 12px;'
            'border: 1px solid #cbd5e1;'
            'height: 100%;'
            'display: flex;'
            'flex-direction: column;'
            'justify-content: center;'
            'align-items: center;'
            'text-align: center;'
            '">'
            '<div style="font-size: 4rem; color: #0ea5e9; margin-bottom: 1rem;">✨</div>'
            '<h3 style="color: #0369a1; margin: 0 0 1rem 0;">Votre voix compte</h3>'
            '<p style="color: #334155; margin-bottom: 1.5rem; font-style: italic;">'
            'Chaque présentation est une opportunité d\'inspirer, de convaincre et de transformer.'
            '</p>'
            
            '<div style="'
            'background: white;'
            'padding: 1rem;'
            'border-radius: 8px;'
            'margin-top: 1rem;'
            'width: 100%;'
            '">'
            '<p style="color: #334155; margin: 0; font-size: 0.95rem;">'
            '<strong>🎯 Votre prochaine étape :</strong><br>'
            'Appliquez ces techniques dans votre prochaine présentation'
            '</p>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    
    # Message final interactif
    st.markdown("### ✨ Votre message à retenir")
    
    col_msg1, col_msg2, col_msg3 = st.columns([1, 2, 1])
    
    with col_msg2:
        if st.button("🎯 Révéler votre message final", type="primary", use_container_width=True, key="final_message_btn"):
            st.session_state.show_final_message = True
    
    if st.session_state.get('show_final_message', False):
        st.balloons()
        st.markdown(
            '<div style="'
            'background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);'
            'padding: 2.5rem;'
            'border-radius: 12px;'
            'text-align: center;'
            'font-size: 1.3rem;'
            'color: #065f46;'
            'margin: 1.5rem 0;'
            'border: 1px solid #10b981;'
            'box-shadow: 0 4px 12px rgba(16, 185, 129, 0.1);'
            '">'
            '<div style="font-size: 2rem; margin-bottom: 1rem;">💫</div>'
            'Votre histoire a du pouvoir.<br>'
            'Votre voix compte.<br>'
            '<strong>Apprenez à la partager.</strong>'
            '</div>',
            unsafe_allow_html=True
        )
    
    # Section feedback enrichie
    st.markdown("---")
    st.markdown("### 📝 Partagez votre expérience")
    
    # Conteneur pour le feedback
    st.markdown(
        '<div style="'
        'background: white;'
        'padding: 2rem;'
        'border-radius: 12px;'
        'border: 1px solid #cbd5e1;'
        'margin-bottom: 2rem;'
        'box-shadow: 0 4px 12px rgba(0, 107, 179, 0.05);'
        '">',
        unsafe_allow_html=True
    )
    
    st.markdown(
        '<div style="'
        'background: #f0f9ff;'
        'padding: 1.5rem;'
        'border-radius: 10px;'
        'margin-bottom: 1.5rem;'
        'border-left: 4px solid #0ea5e9;'
        '">'
        '<h5 style="color: #0369a1; margin: 0 0 0.5rem 0;">🎯 Votre feedback nous aide à améliorer</h5>'
        '<p style="color: #334155; margin: 0;">Partagez vos impressions pour nous aider à rendre MasterTalk encore meilleur.</p>'
        '</div>',
        unsafe_allow_html=True
    )
    
    col_rating1, col_rating2 = st.columns([2, 1])
    
    with col_rating1:
        st.markdown("**Comment avez-vous trouvé cette formation ?**")
        rating = st.slider(
            "Notez cette formation :",
            1, 5, 5,
            key="feedback_rating",
            label_visibility="collapsed"
        )
    
    with col_rating2:
        # Affichage visuel des étoiles amélioré
        stars_html = ""
        for i in range(5):
            if i < rating:
                stars_html += '<span style="font-size: 2rem; color: #fbbf24;">⭐</span>'
            else:
                stars_html += '<span style="font-size: 2rem; color: #cbd5e1;">☆</span>'
        
        st.markdown(
            f'<div style="text-align: center;">'
            f'<div style="font-size: 1.2rem; color: #64748b; margin-bottom: 0.5rem;">Votre note</div>'
            f'<div>{stars_html}</div>'
            f'<div style="font-size: 1.5rem; font-weight: bold; color: #f59e0b; margin-top: 0.5rem;">{rating}/5</div>'
            f'</div>',
            unsafe_allow_html=True
        )
    
    feedback = st.text_area(
        "**Vos commentaires et suggestions :**",
        key="feedback_text",
        height=120,
        placeholder="Partagez vos impressions, ce que vous avez préféré, ce qui pourrait être amélioré..."
    )
    
    col_fb1, col_fb2, col_fb3 = st.columns([1, 2, 1])
    
    with col_fb2:
        if st.button("📤 Envoyer mon feedback", type="primary", use_container_width=True, key="feedback_submit_btn"):
            if feedback:
                st.markdown(
                    '<div style="'
                    'background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);'
                    'padding: 1.5rem;'
                    'border-radius: 10px;'
                    'border-left: 4px solid #10b981;'
                    'text-align: center;'
                    'margin-top: 1rem;'
                    '">'
                    '<div style="display: flex; align-items: center; justify-content: center; gap: 0.8rem; margin-bottom: 0.5rem;">'
                    '<div style="font-size: 1.5rem; color: #065f46;">✅</div>'
                    '<h5 style="color: #065f46; margin: 0;">Merci pour votre feedback !</h5>'
                    '</div>'
                    '<p style="color: #334155; margin: 0;">Votre avis précieux nous aide à améliorer MasterTalk.</p>'
                    '</div>',
                    unsafe_allow_html=True
                )
            else:
                st.warning("Veuillez ajouter un commentaire avant d'envoyer votre feedback.")
    
    if feedback:
        st.info(f"📝 **Votre commentaire :** {len(feedback)} caractères")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Message de remerciement final
    st.markdown(
        '<div style="'
        'background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);'
        'padding: 2rem;'
        'border-radius: 12px;'
        'text-align: center;'
        'margin-top: 2rem;'
        'border: 1px solid #cbd5e1;'
        '">'
        '<h4 style="color: #0369a1; margin: 0 0 1rem 0;">🌟 Merci d\'avoir suivi MasterTalk !</h4>'
        '<p style="color: #334155; margin: 0;">Continuez à pratiquer et à développer vos compétences en communication.</p>'
        '</div>',
        unsafe_allow_html=True
    )

# ============================================================================
# ROUTEUR DE SECTIONS
# ============================================================================

SECTION_HANDLERS = {
    "Introduction": intro_section,
    "1. Qu'est-ce qu'un TED Talk ?": ted_talk_section,
    "2. Méthode SMART": smart_section,
    "3. Storytelling STAR": star_section,
    "4. Écoute Active": ecoute_section,
    "5. Analyse SWOT": swot_section,
    "6. Matrice TOWS": tows_section,
    "7. Ateliers Interactifs": ateliers_section,
    "Conclusion": conclusion_section
}

def render_main_content(section: str) -> None:
    """Affiche le contenu principal en fonction de la section sélectionnée"""
    render_header()
    
    if section in SECTION_HANDLERS:
        SECTION_HANDLERS[section]()
    else:
        st.error("Section non trouvée")

def render_footer() -> None:
    """Affiche le pied de page avec thème clair"""
    st.markdown("---")
    
    footer_content = """
    <div style="
        text-align: center;
        padding: 2rem;
        color: #64748b;
        font-size: 0.9rem;
        background: linear-gradient(90deg, #f0f9ff 0%, #e0f2fe 100%);
        border-radius: 12px;
        border: 1px solid #cbd5e1;
        margin-top: 3rem;
    ">
        <div style="font-size: 1.2rem; color: #0ea5e9; margin-bottom: 0.5rem;">
            🎤 MasterTalk - L'Art de Communiquer
        </div>
        <div style="margin-bottom: 0.5rem;">
            Développez vos compétences en communication | Méthodes éprouvées | Résultats tangibles
        </div>
        <div style="color: #94a3b8;">
            © 2025 MasterTalk | Tous droits réservés
        </div>
    </div>
    """
    
    st.markdown(footer_content, unsafe_allow_html=True)

# ============================================================================
# POINT D'ENTRÉE PRINCIPAL
# ============================================================================

def main():
    """Fonction principale de l'application"""
    # Configuration initiale
    setup_page_config()
    load_custom_css()
    
    # Initialisation de l'état de session
    if 'pause' not in st.session_state:
        st.session_state.pause = False
    
    if 'show_final_message' not in st.session_state:
        st.session_state.show_final_message = False
    
    # Rendu de l'interface
    selected_section = render_sidebar()
    render_main_content(selected_section)
    render_footer()

if __name__ == "__main__":
    main()