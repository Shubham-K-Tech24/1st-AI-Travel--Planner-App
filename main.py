import streamlit as ST
from google import genai
from dotenv import load_dotenv 
import time
load_dotenv()  # Load environment variables from .env file
client = genai.Client()

#ST.title("✈ Romancham Assist")
#ST.caption("Plan your trip with us")
ST.set_page_config(
    page_title="Romancham Travel Assist",
    page_icon="✈",
    layout="wide",

)
ST.markdown("""
    <style>
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.02); }
            100% { transform: scale(1); }
        }
        .animated-title {
            animation: pulse 3s infinite;
            text-align: center;
        }
    </style>
    <div class="animated-title">
        <h1>✈ Romancham Travel Assist</h1>
        <p><b></b>🌏Plan your trips with us</p>
    </div>
""", unsafe_allow_html=True)




# Direct link to your uploaded image
bg_image = " https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?q=80&w=2070&auto=format&fit=crop" # I've re-hosted your image for stability

def set_night_theme(image_url):
    ST.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(10, 10, 30, 0.7), rgba(10, 10, 30, 0.7)), url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        
        /* Neon Glow Title Effect */
        .neon-title {{
            text-align: center;
            font-size: 3.5rem;
            font-weight: 800;
            color: #ffffff;
            text-shadow: 0 0 10px #00d2ff, 0 0 20px #00d2ff, 0 0 30px #00d2ff;
            animation: flicker 2s infinite;
        }}

        @keyframes flicker {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.9; }}
        }}
        
        .subtitle {{
            text-align: center;
            color: #a0d8ef;
            font-size: 1.4rem;
            letter-spacing: 2px;
            font-family: 'Courier New', monospace;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply the theme
set_night_theme(bg_image)



# Add some breathing room
ST.write("")
ST.write("")











Destination=ST.text_input("Where do you want to Travel :")
Days=ST.number_input("For how many days you are planning to Travel :",min_value=1,max_value=30)
Budget=ST.selectbox("Select Budget:",["Luxury","Average","Budgeted"])
Traveling_type=ST.radio("Select your Traveling type:",["Family","Solo","Couple","Friends"])
Prompt=(f'''Your Role: You are a Professional AI Travel Planner, Local Tour Guide, Heritage Expert, and Food Guide.
Your Task:
Create a complete and personalized travel itinerary according to the user's requirements.

USER REQUIREMENTS:

- Destination: {Destination}
- Duration: {Days} days
- Budget Category: {Budget}
- Travelling Type: {Traveling_type}

YOUR RESPONSIBILITIES:

1. DESTINATION INTRODUCTION

- Introduce the destination.
- Explain what makes it special and famous.
- Mention its geographical importance and unique identity.

2. FAMOUS TOURIST ATTRACTIONS

- Suggest the most famous places to visit.
- Include popular tourist attractions and hidden gems.
- Explain why each place is worth visiting.
- Mention entry fees and visiting hours when reliable information is available.

3. HERITAGE AND HISTORICAL PLACES

- Suggest historical monuments, forts, palaces, temples, museums, and heritage sites.
- Explain their historical importance and background.
- Include important cultural and architectural attractions.
- Highlight UNESCO World Heritage Sites if available.

4. FAMOUS LOCAL FOOD

- Suggest traditional and famous dishes of the destination.
- Mention must-try street food and local specialities.
- Recommend popular local restaurants and food markets.
- Explain where visitors can experience authentic local cuisine.

5. DAY-WISE TRAVEL ITINERARY

- Create a detailed itinerary for each day.
- Divide activities into morning, afternoon, and evening.
- Arrange attractions according to their geographical location.
- Include sightseeing, food experiences, and heritage exploration.
- Keep the schedule realistic and comfortable.

6. ACCOMMODATION

- Suggest hotels, hostels, and budget stays.
- Recommend suitable accommodation according to the selected budget.
- Prefer locations close to major attractions.

7. TRANSPORTATION

- Suggest the best transportation options.
- Include local transport facilities.
- Estimate transportation expenses.

8. BUDGET BREAKDOWN

- Accommodation expenses.
- Food expenses.
- Transportation expenses.
- Sightseeing and entry tickets.
- Shopping and miscellaneous expenses.
- Provide the estimated total trip cost.

9. LOCAL CULTURE AND EXPERIENCES

- Explain local traditions, festivals, and customs.
- Suggest famous markets and shopping areas.
- Recommend unique local experiences.
- Mention cultural etiquette and important local rules.

10. TRAVEL TIPS

- Provide safety recommendations.
- Suggest the best time to visit.
- Mention essential items to carry.
- Share useful tips to make the trip convenient.

IMPORTANT INSTRUCTIONS:

- Follow the user's budget and travelling preferences.
- Use Indian Rupees (INR) for estimated costs.
- Prioritize famous attractions, heritage, and authentic food experiences.
- Avoid unnecessarily packed itineraries.
- Do not invent prices, opening hours, ratings, or booking links.
- Clearly distinguish estimated information from verified information.
- Organize the response using headings, tables, and bullet points.

FINAL GOAL:
Make the user experience the destination like a local traveller, not just a tourist.

Provide a complete, practical, informative, and memorable travel plan.
''')


if ST.button("Plan Your Trip"):
    interaction=client.interactions.create(
     model="gemini-3.5-flash-lite",
     input=Prompt
     )

    with ST.spinner("Please wait for a mins...", show_time=True):
        time.sleep(5)
        ST.balloons()
    ST.success("Here is your trip Planning :")
    
    ST.write(interaction.output_text)