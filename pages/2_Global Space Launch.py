from importlib.metadata import metadata
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts
import numpy as np
from scipy import stats
import pydeck as pdk
from PIL import Image

st.set_page_config(page_title="Global Space Launch", page_icon=":rocket:", layout="wide")

st.title("Global Space Launch")

st.image("shift.png")


# MAP


# import streamlit as st
# import pydeck as pdk
# import pandas as pd
# import time

# st.set_page_config(layout="wide")
# st.title("🚀 Global Launch Timeline (1957 - 2025)")

# # --- 1. Your Coordinate Mapping ---
# location_coords = {
#     "Plesetsk Cosmodrome": [64.69703911171159, 40.23202122101674],
#     "Cape Canaveral": [28.496279762592692, -80.57721035730918],
#     "Baikonur Cosmodrome": [45.96971306334741, 63.304277886937385],
#     "Vandenberg": [34.63707751118516, -120.61462487252487],
#     "French Guiana": [5.238019177412824, -52.776268518418654],
#     "Kennedy Space Center": [28.574602148274234, -80.65200491882827],
#     "Jiuquan": [40.986111395894675, 100.20835167725694],
#     "Xichang": [27.900606068582352, 102.24352617642391],
#     "Kapustin Yar": [48.64379836121863, 45.7721244816821],
#     "Taiyuan": [38.848757118763466, 111.60800445417883],
#     "Tanegashima": [30.401876861139385, 130.9774333097495],
#     "Sriharikota": [13.740619507371893, 80.23402800803493],
#     "Uchinoura": [31.25150534828375, 131.0762021966414],
#     "Wallops": [37.9342633502727, -75.47241206565033],
#     "Mahia": [-39.238060638304155, 177.8746161716849],
#     "Wenchang": [19.57689134663915, 110.74800694686337],
#     "Corn Ranch": [31.423072192287673, -104.75717884752879],
#     "Vostochny Cosmodrome": [51.849518067287875, 128.35522818077246],
#     "Semnan": [35.9543550544185, 53.80750192838674],
#     "Yellow Sea": [36.703990039698674, 121.23598239731571],
#     "Palmachim": [31.90644163622597, 34.6933143865769],
#     "Kwajalein Atoll": [8.983651302616964, 167.57807575820812],
#     "Kodiak Launch Complex": [57.43097117418452, -152.35639607941172],
#     "Starbase": [25.99235099359263, -97.18482351352796],
#     "San Marco Platform": [-2.995544841817323, 40.19486645175857],
#     "Woomera": [-31.068851903797793, 136.44265455563396],
#     "Point Mugu": [34.087052955939185, -119.06102115015644],
#     "Edwards AFB": [34.917527442249266, -117.89127770264322],
#     "Naro Space Center": [34.453631884612534, 127.5179146256433],
#     "Spaceport America": [32.9903641484431, -106.97509136279191],
#     "Hammaguir": [30.86787202447907, -3.0436440278099473],
#     "Mojave Air and Space Port": [35.0293525766903, -118.1059669157189],
#     "Sohae": [39.66836829084492, 124.70702819417858],
#     "Gran Canaria": [27.925204643989716, -15.621479594745013],
#     "S. Korea": [36.64325884421309, 127.20682071754388]
# }

# # --- 2. Your Cleaning Function ---
# def clean_location(location):
#     location = str(location).strip()
#     # (Existing cleaning logic...)
#     if "Vandenberg" in location: return "Vandenberg"
#     elif "Cape Canaveral" in location or "CCAFS" in location or "Cape Kennedy" in location: return "Cape Canaveral"
#     elif "Kennedy Space Center" in location or "KSC" in location: return "Kennedy Space Center"
#     elif "Wallops" in location: return "Wallops"
#     elif "Kodiak" in location: return "Kodiak Launch Complex"
#     elif "Starbase" in location: return "Starbase"
#     elif "Corn Ranch" in location or "Van Horn" in location: return "Corn Ranch"
#     elif "Point Mugu" in location: return "Point Mugu"
#     elif "Edwards" in location: return "Edwards AFB"
#     elif "Spaceport America" in location: return "Spaceport America"
#     elif "Mojave" in location: return "Mojave Air and Space Port"
#     elif "Kwajalein" in location: return "Kwajalein Atoll"
#     elif "San Marco" in location: return "San Marco Platform"
#     elif "Plesetsk" in location: return "Plesetsk Cosmodrome"
#     elif "Baikonur" in location or "Tyuratam" in location: return "Baikonur Cosmodrome"
#     elif "Kapustin Yar" in location: return "Kapustin Yar"
#     elif "Vostochny" in location: return "Vostochny Cosmodrome"
#     elif "Jiuquan" in location: return "Jiuquan"
#     elif "Xichang" in location: return "Xichang"
#     elif "Taiyuan" in location: return "Taiyuan"
#     elif "Wenchang" in location: return "Wenchang"
#     elif "Yellow Sea" in location: return "Yellow Sea"
#     elif "Tanegashima" in location: return "Tanegashima"
#     elif "Uchinoura" in location: return "Uchinoura"
#     elif "Sriharikota" in location or "Satish Dhawan" in location: return "Sriharikota"
#     elif "Mahia" in location: return "Mahia"
#     elif "Naro" in location or "Goheung" in location: return "Naro Space Center"
#     elif "S. Korea" in location or "South Korea" in location: return "S. Korea"
#     elif "French Guiana" in location or "Kourou" in location or "Guiana Space Centre" in location: return "French Guiana"
#     elif "Palmachim" in location: return "Palmachim"
#     elif "Semnan" in location: return "Semnan"
#     elif "Woomera" in location: return "Woomera"
#     elif "Hammaguir" in location: return "Hammaguir"
#     elif "Sohae" in location: return "Sohae"
#     elif "Gran Canaria" in location: return "Gran Canaria"
#     return None

# # --- 3. Loading and Preparing Data ---
# @st.cache_data
# def load_and_map_data():
#     try:
#         # Use the correct filename (match your folder)
#         df = pd.read_csv("Data/Master_Space_Data_All.txt")
#     except FileNotFoundError:
#         return pd.DataFrame() # Return empty if file missing

#     # Robust Date Parsing: Specifically handles "Wed May 28, 1958..." 
#     # and "Feb 25 2026..." formats.
#     def extract_year(date_str):
#         try:
#             # We look for a 4-digit number starting with 19 or 20
#             import re
#             match = re.search(r'(19\d{2}|20\d{2})', str(date_str))
#             if match:
#                 return int(match.group(1))
#             return None
#         except:
#             return None

#     df['year'] = df['Datum'].apply(extract_year)
    
#     # Map Locations
#     df["clean_loc"] = df["Location"].apply(clean_location)
#     df["lat"] = df["clean_loc"].apply(lambda x: location_coords[x][0] if x in location_coords else None)
#     df["lon"] = df["clean_loc"].apply(lambda x: location_coords[x][1] if x in location_coords else None)
    
#     # Only keep rows with Year, Lat, and Lon
#     return df.dropna(subset=['year', 'lat', 'lon']).copy()

# space_df = load_and_map_data()

# # --- 4. Main App & Animation ---
# if space_df.empty:
#     st.error("Data could not be loaded or no valid locations/years were found. Check your CSV file and location names.")
# else:
#     min_year = int(space_df['year'].min())
#     max_year = 2025

#     # --- Updated Animation logic for Year-Only View ---
# if st.button('▶️ Start Year-by-Year Animation'):
#     header_placeholder = st.empty()
#     map_placeholder = st.empty()

#     for year in range(min_year, max_year + 1):
#         # CHANGE: Use == instead of <= to show only the current year's data
#         current_data = space_df[space_df['year'] == year]
        
#         # If no launches happened this year, we can either show an empty map 
#         # or skip it. Let's show an empty map so the timeline stays smooth.
#         if current_data.empty:
#             launch_counts = pd.DataFrame(columns=["lat", "lon", "clean_loc", "launch_count", "coordinates", "color", "elevation"])
#         else:
#             launch_counts = (
#                 current_data.groupby(["lat", "lon", "clean_loc"])
#                 .size()
#                 .reset_index(name="launch_count")
#             )
            
#             launch_counts["coordinates"] = launch_counts.apply(lambda r: [r["lon"], r["lat"]], axis=1)
            
#             # Since you're only showing one year, counts will be smaller. 
#             # You might want to increase the elevation multiplier!
#             launch_counts["elevation"] = launch_counts["launch_count"] * 50000 
            
#             # Static Color (Since max_val changes every second, 
#             # static colors prevent the map from "flashing" colors)
#             launch_counts["color"] = [[255, 165, 0, 180]] * len(launch_counts) # Solid Orange

#         layer = pdk.Layer(
#             "ColumnLayer",
#             data=launch_counts,
#             get_position="coordinates",
#             get_elevation="elevation",
#             get_fill_color="color",
#             radius=80000, # Made slightly larger for better visibility
#             extruded=True,
#             pickable=True,
#         )

#         header_placeholder.subheader(f"Global Launches in: {year}")
#         map_placeholder.pydeck_chart(pdk.Deck(
#             layers=[layer],
#             initial_view_state=pdk.ViewState(latitude=20, longitude=10, zoom=1.1, pitch=45),
#             tooltip={"html": "<b>Location:</b> {clean_loc}<br/><b>Launches this year:</b> {launch_count}"}
#         ))
        
#         # You might want a slower speed for this mode (e.g., 0.3)
#         # so people can actually see the "blips" before they disappear.
#         time.sleep(0.5)
#     else:
#         st.info(f"Loaded {len(space_df)} records from {min_year} to {max_year}. Click 'Start' to begin.")



import streamlit as st
import pandas as pd
import pydeck as pdk
import time
import re

st.set_page_config(layout="wide")
st.title("🚀 Global Launch Density Timeline (1957 - 2030)")

# --- 0. Hard Reset Mechanism (Crucial for testing new color logic!) ---
st.sidebar.markdown("### Development Tools")
if st.sidebar.button("Hard Reset App Cache"):
    st.cache_data.clear()
    st.rerun()

# --- 1. Coordinate Mapping ---
location_coords = {
    "Plesetsk Cosmodrome": [64.6970, 40.2320],
    "Cape Canaveral": [28.4962, -80.5772],
    "Baikonur Cosmodrome": [45.9697, 63.3042],
    "Vandenberg": [34.6370, -120.6146],
    "French Guiana": [5.2380, -52.7762],
    "Kennedy Space Center": [28.5746, -80.6520],
    "Jiuquan": [40.9861, 100.2083],
    "Xichang": [27.9006, 102.2435],
    "Kapustin Yar": [48.6437, 45.7721],
    "Taiyuan": [38.8487, 111.6080],
    "Tanegashima": [30.4018, 130.9774],
    "Sriharikota": [13.7406, 80.2340],
    "Uchinoura": [31.2515, 131.0762],
    "Wallops": [37.9342, -75.4724],
    "Mahia": [-39.2380, 177.8746],
    "Wenchang": [19.5768, 110.7480],
    "Corn Ranch": [31.4230, -104.7571],
    "Vostochny Cosmodrome": [51.8495, 128.3552],
    "Semnan": [35.9543, 53.8075],
    "Yellow Sea": [36.7039, 121.2359],
    "Palmachim": [31.9064, 34.6933],
    "Kwajalein Atoll": [8.9836, 167.5780],
    "Kodiak Launch Complex": [57.4309, -152.3563],
    "Starbase": [25.9923, -97.1848],
    "San Marco Platform": [-2.9955, 40.1948],
    "Woomera": [-31.0688, 136.4426],
    "Point Mugu": [34.0870, -119.0610],
    "Edwards AFB": [34.9175, -117.8912],
    "Naro Space Center": [34.4536, 127.5179],
    "Spaceport America": [32.9903, -106.9750],
    "Hammaguir": [30.8678, -3.0436],
    "Mojave Air and Space Port": [35.0293, -118.1059],
    "Sohae": [39.6683, 124.7070],
    "Gran Canaria": [27.9252, -15.6214],
    "S. Korea": [36.6432, 127.2068]
}

# --- 2. Color Gradient Function (New!) ---
def calculate_surge_color(launch_count):
    """
    Calculates a color gradient from Green (Low) -> Orange (Medium) -> Red (High).
    Based on a spectrum of ~1 launch (historical) to ~181 launches (2030 Prediction).
    """
    # Define our range boundaries
    MIN_LAUNCHES = 1
    MAX_LAUNCHES = 181  # Maximum predicted count in your data
    
    # Linear Interpolation of the ratio (0.0 to 1.0)
    # Ensure count is within bounds
    count = max(MIN_LAUNCHES, min(launch_count, MAX_LAUNCHES))
    ratio = (count - MIN_LAUNCHES) / (MAX_LAUNCHES - MIN_LAUNCHES)
    
    # Calculate RGB components: Green (Low) to Red (High)
    # Red component goes UP with count
    red_c = int(255 * ratio)
    # Green component goes DOWN with count
    green_c = int(255 * (1 - ratio))
    # Blue component stays 0 for this gradient
    blue_c = 0
    
    # Return [R, G, B, Alpha]
    return [red_c, green_c, blue_c, 200]


# --- 3. Cleaning Function ---
def clean_location(location):
    location = str(location).strip()
    if "Vandenberg" in location: return "Vandenberg"
    elif any(x in location for x in ["Cape Canaveral", "CCAFS", "Cape Kennedy"]): return "Cape Canaveral"
    elif any(x in location for x in ["Kennedy Space Center", "KSC"]): return "Kennedy Space Center"
    elif "Wallops" in location: return "Wallops"
    elif "Kodiak" in location: return "Kodiak Launch Complex"
    elif "Starbase" in location: return "Starbase"
    elif any(x in location for x in ["Corn Ranch", "Van Horn"]): return "Corn Ranch"
    elif "Point Mugu" in location: return "Point Mugu"
    elif "Edwards" in location: return "Edwards AFB"
    elif "Spaceport America" in location: return "Spaceport America"
    elif "Mojave" in location: return "Mojave Air and Space Port"
    elif "Kwajalein" in location: return "Kwajalein Atoll"
    elif "San Marco" in location: return "San Marco Platform"
    elif "Plesetsk" in location: return "Plesetsk Cosmodrome"
    elif any(x in location for x in ["Baikonur", "Tyuratam"]): return "Baikonur Cosmodrome"
    elif "Kapustin Yar" in location: return "Kapustin Yar"
    elif "Vostochny" in location: return "Vostochny Cosmodrome"
    elif "Jiuquan" in location: return "Jiuquan"
    elif "Xichang" in location: return "Xichang"
    elif "Taiyuan" in location: return "Taiyuan"
    elif "Wenchang" in location: return "Wenchang"
    elif "Yellow Sea" in location: return "Yellow Sea"
    elif "Tanegashima" in location: return "Tanegashima"
    elif "Uchinoura" in location: return "Uchinoura"
    elif any(x in location for x in ["Sriharikota", "Satish Dhawan"]): return "Sriharikota"
    elif "Mahia" in location: return "Mahia"
    elif any(x in location for x in ["Naro", "Goheung"]): return "Naro Space Center"
    elif any(x in location for x in ["S. Korea", "South Korea"]): return "S. Korea"
    elif any(x in location for x in ["French Guiana", "Kourou", "Guiana Space Centre"]): return "French Guiana"
    elif "Palmachim" in location: return "Palmachim"
    elif "Semnan" in location: return "Semnan"
    elif "Woomera" in location: return "Woomera"
    elif "Hammaguir" in location: return "Hammaguir"
    elif "Sohae" in location: return "Sohae"
    elif "Gran Canaria" in location: return "Gran Canaria"
    return None

# --- 4. Loading Data & Predictions ---
@st.cache_data
def load_prepared_data_surge():
    try:
        # Load and clean the CSV
        df = pd.read_csv("data/Master_Space_Data_All.csv")
    except:
        return pd.DataFrame(), pd.DataFrame()

    def extract_year(date_str):
        match = re.search(r'(19\d{2}|20\d{2})', str(date_str))
        return int(match.group(1)) if match else None

    df['year'] = df['Datum'].apply(extract_year)
    df["clean_loc"] = df["Location"].apply(clean_location)
    
    # Filter for valid years and locations
    df = df.dropna(subset=['year', 'clean_loc'])
    
    # Map coordinates
    df["lat"] = df["clean_loc"].apply(lambda x: location_coords.get(x, [None, None])[0])
    df["lon"] = df["clean_loc"].apply(lambda x: location_coords.get(x, [None, None])[1])
    df = df.dropna(subset=['lat', 'lon'])
    
    # PREDICTION DATA (Explicit Counts provided by user)
    predictions = [
        {"year": 2026, "clean_loc": "Cape Canaveral", "launch_count": 95},
        {"year": 2026, "clean_loc": "Vandenberg", "launch_count": 45},
        {"year": 2026, "clean_loc": "Jiuquan", "launch_count": 32},
        {"year": 2026, "clean_loc": "Taiyuan", "launch_count": 14},
        {"year": 2026, "clean_loc": "Wenchang", "launch_count": 8},
        {"year": 2026, "clean_loc": "Xichang", "launch_count": 17},
        {"year": 2026, "clean_loc": "Yellow Sea", "launch_count": 4},
        {"year": 2027, "clean_loc": "Cape Canaveral", "launch_count": 110},
        {"year": 2027, "clean_loc": "Vandenberg", "launch_count": 55},
        {"year": 2027, "clean_loc": "Jiuquan", "launch_count": 36},
        {"year": 2027, "clean_loc": "Taiyuan", "launch_count": 16},
        {"year": 2027, "clean_loc": "Wenchang", "launch_count": 9},
        {"year": 2027, "clean_loc": "Xichang", "launch_count": 17},
        {"year": 2027, "clean_loc": "Yellow Sea", "launch_count": 5},
        {"year": 2028, "clean_loc": "Cape Canaveral", "launch_count": 130},
        {"year": 2028, "clean_loc": "Vandenberg", "launch_count": 65},
        {"year": 2028, "clean_loc": "Jiuquan", "launch_count": 40},
        {"year": 2028, "clean_loc": "Taiyuan", "launch_count": 18},
        {"year": 2028, "clean_loc": "Wenchang", "launch_count": 10},
        {"year": 2028, "clean_loc": "Xichang", "launch_count": 18},
        {"year": 2028, "clean_loc": "Yellow Sea", "launch_count": 6},
        {"year": 2029, "clean_loc": "Cape Canaveral", "launch_count": 150},
        {"year": 2029, "clean_loc": "Vandenberg", "launch_count": 75},
        {"year": 2029, "clean_loc": "Jiuquan", "launch_count": 44},
        {"year": 2029, "clean_loc": "Taiyuan", "launch_count": 20},
        {"year": 2029, "clean_loc": "Wenchang", "launch_count": 11},
        {"year": 2029, "clean_loc": "Xichang", "launch_count": 19},
        {"year": 2029, "clean_loc": "Yellow Sea", "launch_count": 7},
        {"year": 2030, "clean_loc": "Cape Canaveral", "launch_count": 180},
        {"year": 2030, "clean_loc": "Vandenberg", "launch_count": 90},
        {"year": 2030, "clean_loc": "Jiuquan", "launch_count": 48},
        {"year": 2030, "clean_loc": "Taiyuan", "launch_count": 22},
        {"year": 2030, "clean_loc": "Wenchang", "launch_count": 12},
        {"year": 2030, "clean_loc": "Xichang", "launch_count": 19},
        {"year": 2030, "clean_loc": "Yellow Sea", "launch_count": 8}
    ]
    
    pdf = pd.DataFrame(predictions)
    pdf["lat"] = pdf["clean_loc"].apply(lambda x: location_coords[x][0])
    pdf["lon"] = pdf["clean_loc"].apply(lambda x: location_coords[x][1])
    
    return df.copy(), pdf

space_df, predict_df = load_prepared_data_surge()

# --- 5. Main App & Animation ---
if space_df.empty and predict_df.empty:
    st.error("No data found. Ensure your CSV is in 'data/Master_Space_Data_All.csv' and hard reset cache.")
else:
    # Determine the timeline range correctly
    if not space_df.empty:
        min_year = int(space_df['year'].min())
    else:
        min_year = 2026
    
    max_year = 2030

    if st.button('▶️ Start Year-by-Year Animation'):
        header_placeholder = st.empty()
        map_placeholder = st.empty()

        for year in range(min_year, max_year + 1):
            if year <= 2025:
                # Historical processing
                current_data = space_df[space_df['year'] == year]
                if current_data.empty: continue
                launch_counts = current_data.groupby(["lat", "lon", "clean_loc"]).size().reset_index(name="launch_count")
                status_text = "Historical"
            else:
                # Prediction processing
                launch_counts = predict_df[predict_df['year'] == year].copy()
                status_text = "PREDICTED SURGE"

            if not launch_counts.empty:
                # Prepare Pydeck Visuals
                launch_counts["coordinates"] = launch_counts.apply(lambda r: [r["lon"], r["lat"]], axis=1)
                
                # Dynamic Elevation Scaling (Slightly reduced to avoid camera clipping)
                launch_counts["elevation"] = launch_counts["launch_count"] * 10000 
                
                # --- Dynamic Color Scaling (New!) ---
                launch_counts["color"] = launch_counts["launch_count"].apply(calculate_surge_color)

                layer = pdk.Layer(
                    "ColumnLayer",
                    data=launch_counts,
                    get_position="coordinates",
                    get_elevation="elevation",
                    get_fill_color="color",
                    radius=80000,
                    extruded=True,
                    pickable=True,
                    auto_highlight=True,
                )

                header_placeholder.subheader(f"Global Launches in: {year} ({status_text})")
                
                # Added White border to the columns to standardize the radius look
                map_placeholder.pydeck_chart(pdk.Deck(
                    layers=[layer],
                    initial_view_state=pdk.ViewState(latitude=20, longitude=10, zoom=1.1, pitch=45),
                    tooltip={"html": "<b>Location:</b> {clean_loc}<br/><b>Count:</b> {launch_count}"}
                ))
            
            time.sleep(0.3)
    else:
        st.info(f"Historical Data Found from {min_year}. Predictions through {max_year}. Color shifts Green -> Red as density increases. Click 'Start' to begin.")