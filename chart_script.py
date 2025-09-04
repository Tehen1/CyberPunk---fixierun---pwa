import plotly.express as px
import pandas as pd

# Constants for repeated labels
TECH_STACK = "Tech Stack"
KEY_METRICS = "Key Metrics"

# Create hierarchical data for sunburst chart
data = []

# Key metrics (outer ring - most important)
data.extend([
    {"category": KEY_METRICS, "subcategory": "Total Rides", "value": 3932, "label": "3.9k Rides", "full_path": "Fixie PWA - Key Metrics - Total Rides"},
    {"category": KEY_METRICS, "subcategory": "Distance", "value": 2651, "label": "10.6k km", "full_path": "Fixie PWA - Key Metrics - Distance"},
    {"category": KEY_METRICS, "subcategory": "FIXIE Tokens", "value": 2137, "label": "8.5k Tokens", "full_path": "Fixie PWA - Key Metrics - FIXIE Tokens"},
    {"category": KEY_METRICS, "subcategory": "CO2 Saved", "value": 318, "label": "1.3k kg", "full_path": "Fixie PWA - Key Metrics - CO2 Saved"},
])

# Urban Performance
data.extend([
    {"category": "Performance", "subcategory": "Regularity", "value": 250, "label": "100%", "full_path": "Fixie PWA - Performance - Regularity"},
    {"category": "Performance", "subcategory": "Exploration", "value": 183, "label": "73%", "full_path": "Fixie PWA - Performance - Exploration"},
    {"category": "Performance", "subcategory": "Efficiency", "value": 175, "label": "70%", "full_path": "Fixie PWA - Performance - Efficiency"},
    {"category": "Performance", "subcategory": "Endurance", "value": 67, "label": "27%", "full_path": "Fixie PWA - Performance - Endurance"},
])

# Core Architecture Modules
data.extend([
    {"category": "Core Modules", "subcategory": "GPS Engine", "value": 300, "label": "GPS Track", "full_path": "Fixie PWA - Core Modules - GPS Engine"},
    {"category": "Core Modules", "subcategory": "Workout Eng", "value": 280, "label": "Workout", "full_path": "Fixie PWA - Core Modules - Workout Eng"},
    {"category": "Core Modules", "subcategory": "Token Econ", "value": 260, "label": "Economics", "full_path": "Fixie PWA - Core Modules - Token Econ"},
    {"category": "Core Modules", "subcategory": "Analytics", "value": 240, "label": "Analytics", "full_path": "Fixie PWA - Core Modules - Analytics"},
])

# UI Architecture Layers  
data.extend([
    {"category": "UI Layers", "subcategory": "PWA Shell", "value": 200, "label": "PWA Core", "full_path": "Fixie PWA - UI Layers - PWA Shell"},
    {"category": "UI Layers", "subcategory": "Navigation", "value": 180, "label": "Nav System", "full_path": "Fixie PWA - UI Layers - Navigation"},
    {"category": "UI Layers", "subcategory": "Views", "value": 160, "label": "5 Views", "full_path": "Fixie PWA - UI Layers - Views"},
    {"category": "UI Layers", "subcategory": "Components", "value": 140, "label": "UI Comps", "full_path": "Fixie PWA - UI Layers - Components"},
])

# Technology Stack
data.extend([
    {"category": TECH_STACK, "subcategory": "Frontend", "value": 120, "label": "HTML5/JS", "full_path": "Fixie PWA - Tech Stack - Frontend"},
    {"category": TECH_STACK, "subcategory": "Charts", "value": 100, "label": "Chart.js", "full_path": "Fixie PWA - Tech Stack - Charts"},
    {"category": TECH_STACK, "subcategory": "Maps", "value": 90, "label": "Leaflet", "full_path": "Fixie PWA - Tech Stack - Maps"},
    {"category": TECH_STACK, "subcategory": "PWA APIs", "value": 80, "label": "Service W", "full_path": "Fixie PWA - Tech Stack - PWA APIs"},
])

# Security & Optimization
data.extend([
    {"category": "Security", "subcategory": "HTTPS", "value": 70, "label": "HTTPS", "full_path": "Fixie PWA - Security - HTTPS"},
    {"category": "Security", "subcategory": "Encryption", "value": 60, "label": "Crypto", "full_path": "Fixie PWA - Security - Encryption"},
    {"category": "Security", "subcategory": "Offline", "value": 55, "label": "Offline", "full_path": "Fixie PWA - Security - Offline"},
    {"category": "Security", "subcategory": "Validation", "value": 50, "label": "Validate", "full_path": "Fixie PWA - Security - Validation"},
])

# Create DataFrame
df = pd.DataFrame(data)

# Create path column for sunburst
df['path'] = 'Fixie PWA - ' + df['category'] + ' - ' + df['subcategory']

# Create custom color mapping for cyber/neon theme
color_map = {
    KEY_METRICS: '#1FB8CD',    # Strong cyan
    'Performance': '#DB4545',    # Bright red  
    'Core Modules': '#2E8B57',   # Sea green
    'UI Layers': '#D2BA4C',      # Moderate yellow
    TECH_STACK: '#5D878F',     # Cyan
    'Security': '#B4413C'        # Moderate red
}

# Create sunburst chart
fig = px.sunburst(
    df,
    path=['category', 'subcategory'],
    values='value',
    color='category',
    color_discrete_map=color_map,
    title="Fixie PWA Architecture"
)

# Update layout for cyber aesthetic
fig.update_layout(
    
    title_fontcolor='white',
    paper_bgcolor='#0a0a0a',  # Dark background
    title="Fixie PWA Architecture",
    width=1000,
    height=600,
    title_x=0.5,
    title_y=0.95,
    title_xanchor='center',
    title_yanchor='top',
    title_fontcolor='white',
    paper_bgcolor='#0a0a0a',  # Dark background
    plot_bgcolor='#0a0a0a'
)

# Update traces for better styling
fig.update_traces(
    textinfo="label+value",
    textposition="inside",
    hovertemplate='<b>%{label}</b><br>Value: %{value}<br>Path: %{id}<extra></extra>',
    maxdepth=3
)

# Save the chart
fig.write_image("fixie_architecture_dashboard.png")