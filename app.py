from flask import Flask, render_template_string, request, jsonify
import json

app = Flask(__name__)

# Enhanced country dataset with 8 countries and high-quality working images
countries_data = [
    {
        'name': 'France',
        'rank': 1,
        'most_visited': True,
        'best_places': ['Eiffel Tower', 'Louvre Museum', 'French Riviera', 'Mont Saint-Michel', 'Loire Valley', 'Champs-Élysées', 'Provence Lavender Fields'],
        'image': 'https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg?w=1200&h=800&fit=crop',
        'thumbnail': 'https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg?w=500&h=350&fit=crop',
        'description': 'France is the world\'s most visited country, offering unparalleled art, architecture, cuisine, and romance. From the iconic Eiffel Tower to the sun-drenched French Riviera, every region tells a unique story.',
        'cuisine': ['Croissant', 'Baguette', 'Coq au Vin', 'Ratatouille', 'Crème Brûlée', 'Escargot', 'Macarons'],
        'best_time': 'April-June & September-October',
        'currency': 'Euro (EUR)',
        'language': 'French',
        'fun_fact': 'France has over 40,000 châteaux (castles) scattered across its countryside!',
        'airport': 'Charles de Gaulle (CDG), Paris',
        'famous_for': 'Wine, Fashion, Art, Romance',
        'coordinates': [48.8566, 2.3522]
    },
    {
        'name': 'Spain',
        'rank': 2,
        'most_visited': False,
        'best_places': ['Sagrada Familia', 'Alhambra', 'Park Güell', 'Plaza Mayor', 'Ibiza Beaches', 'Seville Cathedral', 'Camino de Santiago'],
        'image': 'https://images.pexels.com/photos/1285625/pexels-photo-1285625.jpeg?w=1200&h=800&fit=crop',
        'thumbnail': 'https://images.pexels.com/photos/1285625/pexels-photo-1285625.jpeg?w=500&h=350&fit=crop',
        'description': 'Spain is a vibrant tapestry of cultures, from Gaudí\'s architectural wonders in Barcelona to the passionate flamenco of Andalusia. Experience world-class beaches, festivals, and cuisine.',
        'cuisine': ['Paella', 'Tapas', 'Jamón Ibérico', 'Gazpacho', 'Churros', 'Patatas Bravas', 'Sangria'],
        'best_time': 'March-May & September-November',
        'currency': 'Euro (EUR)',
        'language': 'Spanish',
        'fun_fact': 'Spain has the second highest number of UNESCO World Heritage sites after Italy!',
        'airport': 'Adolfo Suárez Madrid-Barajas (MAD)',
        'famous_for': 'Flamenco, Football, Siesta, Beaches',
        'coordinates': [40.4168, -3.7038]
    },
    {
        'name': 'Italy',
        'rank': 3,
        'most_visited': False,
        'best_places': ['Colosseum', 'Venice Canals', 'Florence Duomo', 'Amalfi Coast', 'Cinque Terre', 'Pompeii', 'Leaning Tower of Pisa'],
        'image': 'https://images.pexels.com/photos/1797161/pexels-photo-1797161.jpeg?w=1200&h=800&fit=crop',
        'thumbnail': 'https://images.pexels.com/photos/1797161/pexels-photo-1797161.jpeg?w=500&h=350&fit=crop',
        'description': 'Italy is a living museum of art, history, and gastronomy. From ancient Roman ruins to Renaissance masterpieces, every corner tells stories of emperors, artists, and culinary excellence.',
        'cuisine': ['Pizza', 'Pasta', 'Gelato', 'Risotto', 'Tiramisu', 'Lasagna', 'Espresso'],
        'best_time': 'April-June & September-October',
        'currency': 'Euro (EUR)',
        'language': 'Italian',
        'fun_fact': 'Italy has 58 UNESCO World Heritage sites, more than any other country!',
        'airport': 'Leonardo da Vinci-Fiumicino (FCO), Rome',
        'famous_for': 'Pasta, Pizza, Renaissance Art, Fashion',
        'coordinates': [41.9028, 12.4964]
    },
    {
        'name': 'Japan',
        'rank': 4,
        'most_visited': False,
        'best_places': ['Mount Fuji', 'Fushimi Inari Shrine', 'Shibuya Crossing', 'Osaka Castle', 'Arashiyama Bamboo Grove', 'Himeji Castle', 'Nara Park'],
        'image': 'https://images.pexels.com/photos/2614818/pexels-photo-2614818.jpeg?w=1200&h=800&fit=crop',
        'thumbnail': 'https://images.pexels.com/photos/2614818/pexels-photo-2614818.jpeg?w=500&h=350&fit=crop',
        'description': 'Japan perfectly balances ancient traditions with futuristic innovation. Experience serene temples, vibrant cities, cherry blossoms, and world-renowned hospitality.',
        'cuisine': ['Sushi', 'Ramen', 'Tempura', 'Matcha', 'Takoyaki', 'Okonomiyaki', 'Mochi'],
        'best_time': 'March-May & September-November',
        'currency': 'Japanese Yen (JPY)',
        'language': 'Japanese',
        'fun_fact': 'Japan has over 5 million vending machines, one for every 24 people!',
        'airport': 'Narita International (NRT), Tokyo',
        'famous_for': 'Cherry Blossoms, Technology, Anime, Sushi',
        'coordinates': [35.6762, 139.6503]
    },
    {
        'name': 'Australia',
        'rank': 5,
        'most_visited': False,
        'best_places': ['Sydney Opera House', 'Great Barrier Reef', 'Uluru', 'Great Ocean Road', 'Bondi Beach', 'Daintree Rainforest', 'Kangaroo Island'],
        'image': 'https://images.pexels.com/photos/1659437/pexels-photo-1659437.jpeg?w=1200&h=800&fit=crop',
        'thumbnail': 'https://images.pexels.com/photos/1659437/pexels-photo-1659437.jpeg?w=500&h=350&fit=crop',
        'description': 'Australia is a land of extraordinary natural beauty, from the iconic Sydney Opera House to the ancient wonders of the Outback. Adventure awaits with unique wildlife and stunning coastlines.',
        'cuisine': ['Meat Pie', 'Vegemite', 'Barramundi', 'Lamington', 'Pavlova', 'Flat White Coffee'],
        'best_time': 'September-November & March-May',
        'currency': 'Australian Dollar (AUD)',
        'language': 'English',
        'fun_fact': 'Australia has 10,685 beaches - you could visit a new beach every day for 29 years!',
        'airport': 'Sydney Kingsford Smith (SYD)',
        'famous_for': 'Kangaroos, Great Barrier Reef, Beaches, Surfing',
        'coordinates': [-33.8688, 151.2093]
    },
    {
        'name': 'Thailand',
        'rank': 6,
        'most_visited': False,
        'best_places': ['Bangkok', 'Phuket', 'Chiang Mai', 'Krabi', 'Koh Samui', 'Ayutthaya', 'Phi Phi Islands'],
        'image': 'https://images.pexels.com/photos/1450353/pexels-photo-1450353.jpeg?w=1200&h=800&fit=crop',
        'thumbnail': 'https://images.pexels.com/photos/1450353/pexels-photo-1450353.jpeg?w=500&h=350&fit=crop',
        'description': 'Thailand is a tropical paradise known for its stunning beaches, ornate temples, vibrant street food, and warm hospitality. From bustling Bangkok to serene island escapes.',
        'cuisine': ['Pad Thai', 'Tom Yum Goong', 'Green Curry', 'Mango Sticky Rice', 'Som Tam', 'Satay'],
        'best_time': 'November-February',
        'currency': 'Thai Baht (THB)',
        'language': 'Thai',
        'fun_fact': 'Thailand is the only country in Southeast Asia that was never colonized by European powers!',
        'airport': 'Suvarnabhumi Airport (BKK), Bangkok',
        'famous_for': 'Beaches, Temples, Street Food, Massage',
        'coordinates': [13.7563, 100.5018]
    },
    {
        'name': 'Greece',
        'rank': 7,
        'most_visited': False,
        'best_places': ['Santorini', 'Athens Acropolis', 'Mykonos', 'Crete', 'Rhodes', 'Meteora', 'Corfu'],
        'image': 'https://images.pexels.com/photos/1496372/pexels-photo-1496372.jpeg?w=1200&h=800&fit=crop',
        'thumbnail': 'https://images.pexels.com/photos/1496372/pexels-photo-1496372.jpeg?w=500&h=350&fit=crop',
        'description': 'Greece is the cradle of Western civilization, offering ancient ruins, stunning islands, crystal-clear waters, and delicious Mediterranean cuisine.',
        'cuisine': ['Moussaka', 'Souvlaki', 'Greek Salad', 'Baklava', 'Tzatziki', 'Feta Cheese'],
        'best_time': 'April-October',
        'currency': 'Euro (EUR)',
        'language': 'Greek',
        'fun_fact': 'Greece has over 6,000 islands, but only about 227 are inhabited!',
        'airport': 'Athens International (ATH)',
        'famous_for': 'Ancient History, Islands, Olive Oil, Philosophy',
        'coordinates': [37.9838, 23.7275]
    },
    {
        'name': 'Brazil',
        'rank': 8,
        'most_visited': False,
        'best_places': ['Christ the Redeemer', 'Copacabana Beach', 'Amazon Rainforest', 'Iguazu Falls', 'Salvador', 'Fernando de Noronha', 'Sugarloaf Mountain'],
        'image': 'https://images.pexels.com/photos/2859169/pexels-photo-2859169.jpeg?w=1200&h=800&fit=crop',
        'thumbnail': 'https://images.pexels.com/photos/2859169/pexels-photo-2859169.jpeg?w=500&h=350&fit=crop',
        'description': 'Brazil is a vibrant country of samba, soccer, and stunning natural wonders. From the Amazon rainforest to the iconic beaches of Rio de Janeiro.',
        'cuisine': ['Feijoada', 'Pão de Queijo', 'Acarajé', 'Brigadeiro', 'Caipirinha', 'Moqueca'],
        'best_time': 'December-March',
        'currency': 'Brazilian Real (BRL)',
        'language': 'Portuguese',
        'fun_fact': 'Brazil has the largest Japanese population outside of Japan!',
        'airport': 'São Paulo-Guarulhos (GRU)',
        'famous_for': 'Carnival, Soccer, Amazon Rainforest, Beaches',
        'coordinates': [-22.9068, -43.1729]
    }
]

# For search functionality
country_search_data = [
    {'name': 'France', 'region': 'Europe', 'capital': 'Paris', 'population': '67.4M', 'language': 'French', 'currency': 'Euro', 'image': 'https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg?w=400&h=250&fit=crop'},
    {'name': 'Spain', 'region': 'Europe', 'capital': 'Madrid', 'population': '47.4M', 'language': 'Spanish', 'currency': 'Euro', 'image': 'https://images.pexels.com/photos/1285625/pexels-photo-1285625.jpeg?w=400&h=250&fit=crop'},
    {'name': 'Italy', 'region': 'Europe', 'capital': 'Rome', 'population': '59.5M', 'language': 'Italian', 'currency': 'Euro', 'image': 'https://images.pexels.com/photos/1797161/pexels-photo-1797161.jpeg?w=400&h=250&fit=crop'},
    {'name': 'Japan', 'region': 'Asia', 'capital': 'Tokyo', 'population': '125.8M', 'language': 'Japanese', 'currency': 'Yen', 'image': 'https://images.pexels.com/photos/2614818/pexels-photo-2614818.jpeg?w=400&h=250&fit=crop'},
    {'name': 'Australia', 'region': 'Oceania', 'capital': 'Canberra', 'population': '25.7M', 'language': 'English', 'currency': 'AUD', 'image': 'https://images.pexels.com/photos/1659437/pexels-photo-1659437.jpeg?w=400&h=250&fit=crop'},
    {'name': 'Thailand', 'region': 'Asia', 'capital': 'Bangkok', 'population': '69.9M', 'language': 'Thai', 'currency': 'Baht', 'image': 'https://images.pexels.com/photos/1450353/pexels-photo-1450353.jpeg?w=400&h=250&fit=crop'},
    {'name': 'Greece', 'region': 'Europe', 'capital': 'Athens', 'population': '10.4M', 'language': 'Greek', 'currency': 'Euro', 'image': 'https://images.pexels.com/photos/1496372/pexels-photo-1496372.jpeg?w=400&h=250&fit=crop'},
    {'name': 'Brazil', 'region': 'South America', 'capital': 'Brasília', 'population': '213.9M', 'language': 'Portuguese', 'currency': 'Real', 'image': 'https://images.pexels.com/photos/2859169/pexels-photo-2859169.jpeg?w=400&h=250&fit=crop'}
]

# Carousel images with all working URLs
carousel_images = [
    {'url': 'https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg?w=1400&h=550&fit=crop', 'caption': 'Eiffel Tower, Paris, France', 'country': 'France', 'description': 'The iconic symbol of romance and elegance'},
    {'url': 'https://images.pexels.com/photos/1797161/pexels-photo-1797161.jpeg?w=1400&h=550&fit=crop', 'caption': 'Colosseum, Rome, Italy', 'country': 'Italy', 'description': 'Ancient wonder of the Roman Empire'},
    {'url': 'https://images.pexels.com/photos/1285625/pexels-photo-1285625.jpeg?w=1400&h=550&fit=crop', 'caption': 'Sagrada Familia, Barcelona, Spain', 'country': 'Spain', 'description': 'Gaudí\'s architectural masterpiece'},
    {'url': 'https://images.pexels.com/photos/2614818/pexels-photo-2614818.jpeg?w=1400&h=550&fit=crop', 'caption': 'Mount Fuji, Japan', 'country': 'Japan', 'description': 'Sacred mountain and cultural icon'},
    {'url': 'https://images.pexels.com/photos/1659437/pexels-photo-1659437.jpeg?w=1400&h=550&fit=crop', 'caption': 'Sydney Opera House, Australia', 'country': 'Australia', 'description': 'Architectural marvel by the harbor'},
    {'url': 'https://images.pexels.com/photos/1450353/pexels-photo-1450353.jpeg?w=1400&h=550&fit=crop', 'caption': 'Phuket Beaches, Thailand', 'country': 'Thailand', 'description': 'Tropical paradise with crystal clear waters'},
    {'url': 'https://images.pexels.com/photos/1496372/pexels-photo-1496372.jpeg?w=1400&h=550&fit=crop', 'caption': 'Santorini, Greece', 'country': 'Greece', 'description': 'Stunning white-washed buildings and blue domes'},
    {'url': 'https://images.pexels.com/photos/2859169/pexels-photo-2859169.jpeg?w=1400&h=550&fit=crop', 'caption': 'Christ the Redeemer, Rio, Brazil', 'country': 'Brazil', 'description': 'One of the New Seven Wonders of the World'}
]

# Travel stats
travel_stats = [
    {'value': '195+', 'label': 'Countries', 'icon': 'fas fa-globe'},
    {'value': '1.4B+', 'label': 'Annual Travelers', 'icon': 'fas fa-users'},
    {'value': '2,000+', 'label': 'Destinations', 'icon': 'fas fa-map-marker-alt'},
    {'value': '24/7', 'label': 'Support', 'icon': 'fas fa-headset'}
]

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>GlobeTrotter Elite | Interactive World Travel Guide</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #ffffff;
            overflow-x: hidden;
        }

        /* Clear Beautiful Background Image */
        .bg-image {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -2;
            background-image: url('https://images.pexels.com/photos/2387873/pexels-photo-2387873.jpeg?w=1920&h=1080&fit=crop');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        
        .bg-image::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.65);
            pointer-events: none;
        }
        
        /* Animated overlay */
        .animated-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            background: radial-gradient(circle at 20% 50%, rgba(74,158,255,0.08) 0%, transparent 70%);
            animation: pulseGlow 8s ease-in-out infinite;
        }
        
        @keyframes pulseGlow {
            0%, 100% { opacity: 0.4; }
            50% { opacity: 0.7; }
        }

        /* Main container */
        .main-wrapper {
            max-width: 1400px;
            margin: 0 auto;
            padding: 1.2rem 2rem 3rem;
            position: relative;
            z-index: 2;
        }

        /* Glass Header */
        .glass-header {
            backdrop-filter: blur(15px);
            background: rgba(15, 25, 45, 0.55);
            border-radius: 2rem;
            padding: 0.8rem 2rem;
            margin-bottom: 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
            border: 1px solid rgba(72, 187, 255, 0.3);
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        }
        
        .logo {
            font-size: 1.8rem;
            font-weight: 800;
            background: linear-gradient(135deg, #a5f0ff, #4a9eff, #7c3aed);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            animation: gradientShift 3s ease infinite;
            background-size: 200% auto;
        }
        
        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        .logo i {
            background: none;
            -webkit-background-clip: unset;
            color: #4a9eff;
        }
        
        .search-form {
            display: flex;
            gap: 0.6rem;
        }
        
        .search-input {
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(79, 163, 255, 0.5);
            border-radius: 3rem;
            padding: 0.7rem 1.4rem;
            color: white;
            font-size: 0.9rem;
            width: 280px;
            outline: none;
            transition: all 0.3s;
        }
        
        .search-input:focus {
            border-color: #4a9eff;
            background: rgba(255,255,255,0.2);
            box-shadow: 0 0 20px rgba(74,158,255,0.3);
        }
        
        .search-btn {
            background: linear-gradient(135deg, #2c7da0, #1f5e7e);
            border: none;
            border-radius: 3rem;
            padding: 0.7rem 1.5rem;
            color: white;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .search-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(44,125,160,0.4);
        }
        
        .nav-links {
            display: flex;
            gap: 1.8rem;
        }
        
        .nav-links a {
            color: #ccdeff;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s;
            position: relative;
        }
        
        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0%;
            height: 2px;
            background: linear-gradient(90deg, #4a9eff, #7c3aed);
            transition: width 0.3s;
        }
        
        .nav-links a:hover::after {
            width: 100%;
        }
        
        .nav-links a:hover {
            color: #7bc5ff;
        }

        /* Hero Stats */
        .hero-stats {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 1.5rem;
            margin-bottom: 2rem;
            padding: 1rem;
        }
        
        .stat-card {
            flex: 1;
            min-width: 150px;
            text-align: center;
            background: rgba(255,255,255,0.08);
            backdrop-filter: blur(10px);
            border-radius: 1.5rem;
            padding: 1.2rem;
            border: 1px solid rgba(255,255,255,0.15);
            transition: all 0.3s;
        }
        
        .stat-card:hover {
            transform: translateY(-5px);
            background: rgba(255,255,255,0.15);
            border-color: rgba(74,158,255,0.5);
        }
        
        .stat-card i {
            font-size: 2rem;
            color: #4a9eff;
            margin-bottom: 0.5rem;
        }
        
        .stat-value {
            font-size: 1.8rem;
            font-weight: 800;
        }
        
        .stat-label {
            font-size: 0.85rem;
            color: #a0b4d7;
        }

        /* 3D World Map Container */
        .world-map-container {
            margin-bottom: 3rem;
            border-radius: 2rem;
            overflow: hidden;
            background: rgba(0,0,0,0.3);
            border: 1px solid rgba(74,158,255,0.3);
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        }
        
        .map-header {
            padding: 1rem 1.5rem;
            background: linear-gradient(135deg, rgba(74,158,255,0.2), rgba(124,58,237,0.1));
            border-bottom: 1px solid rgba(74,158,255,0.3);
        }
        
        .map-header h3 {
            font-size: 1.2rem;
            font-weight: 600;
        }
        
        .map-header h3 i {
            color: #4a9eff;
            margin-right: 0.5rem;
        }
        
        #world-map {
            width: 100%;
            height: 500px;
            background: rgba(10, 20, 40, 0.6);
        }
        
        .map-controls {
            padding: 0.8rem 1.5rem;
            background: rgba(0,0,0,0.5);
            display: flex;
            gap: 1rem;
            justify-content: center;
        }
        
        .map-controls button {
            background: rgba(74,158,255,0.3);
            border: 1px solid rgba(74,158,255,0.5);
            color: white;
            padding: 0.4rem 1rem;
            border-radius: 2rem;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .map-controls button:hover {
            background: rgba(74,158,255,0.6);
        }

        /* Carousel */
        .carousel-container {
            position: relative;
            margin-bottom: 3rem;
            border-radius: 2rem;
            overflow: hidden;
            box-shadow: 0 25px 45px rgba(0,0,0,0.4);
            border: 1px solid rgba(255,255,255,0.2);
        }
        
        .carousel-slides {
            display: flex;
            transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .carousel-slide {
            min-width: 100%;
            position: relative;
        }
        
        .carousel-slide img {
            width: 100%;
            height: 500px;
            object-fit: cover;
        }
        
        .carousel-caption {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: linear-gradient(transparent, rgba(0,0,0,0.9));
            padding: 2rem;
            color: white;
        }
        
        .carousel-caption h3 {
            font-size: 2rem;
            margin-bottom: 0.3rem;
            font-weight: 700;
        }
        
        .carousel-caption p {
            font-size: 1rem;
            opacity: 0.9;
        }
        
        .carousel-btn {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background: rgba(0,0,0,0.6);
            backdrop-filter: blur(5px);
            color: white;
            border: none;
            padding: 1rem 1.3rem;
            cursor: pointer;
            font-size: 1.5rem;
            transition: all 0.3s;
            z-index: 10;
            border-radius: 50%;
        }
        
        .carousel-btn:hover {
            background: rgba(74,158,255,0.8);
            transform: translateY(-50%) scale(1.05);
        }
        
        .carousel-prev {
            left: 20px;
        }
        
        .carousel-next {
            right: 20px;
        }
        
        .carousel-dots {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 12px;
            z-index: 10;
        }
        
        .dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: rgba(255,255,255,0.5);
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .dot.active {
            background: #4a9eff;
            width: 25px;
            border-radius: 10px;
        }

        /* Section Title */
        .section-title {
            font-size: 2rem;
            font-weight: 700;
            margin: 2.5rem 0 1.5rem 0;
            border-left: 5px solid #3b82f6;
            padding-left: 1rem;
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        /* Country Cards */
        .country-showcase {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
            gap: 2rem;
        }
        
        .country-card {
            background: rgba(18, 28, 50, 0.8);
            backdrop-filter: blur(10px);
            border-radius: 1.5rem;
            overflow: hidden;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid rgba(59,130,246,0.3);
            cursor: pointer;
            position: relative;
        }
        
        .country-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(74,158,255,0.1), transparent);
            opacity: 0;
            transition: opacity 0.4s;
        }
        
        .country-card:hover::before {
            opacity: 1;
        }
        
        .country-card:hover {
            transform: translateY(-12px) scale(1.02);
            border-color: rgba(59,130,246,0.8);
            box-shadow: 0 25px 40px rgba(0,0,0,0.4);
        }
        
        .country-card img {
            width: 100%;
            height: 240px;
            object-fit: cover;
            transition: transform 0.4s;
        }
        
        .country-card:hover img {
            transform: scale(1.05);
        }
        
        .card-content {
            padding: 1.3rem 1.5rem 1.5rem;
            position: relative;
        }
        
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.8rem;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        
        .country-name {
            font-size: 1.6rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .most-badge {
            background: linear-gradient(135deg, #fbbf24, #f59e0b);
            color: #1e1e2a;
            padding: 0.25rem 0.9rem;
            border-radius: 40px;
            font-size: 0.7rem;
            font-weight: 800;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { box-shadow: 0 0 0 0 rgba(251,191,36,0.4); }
            50% { box-shadow: 0 0 0 5px rgba(251,191,36,0); }
        }
        
        .rank-badge {
            background: linear-gradient(135deg, #1e2a47, #0f172a);
            padding: 0.25rem 0.9rem;
            border-radius: 40px;
            font-size: 0.8rem;
            font-weight: 600;
        }
        
        .places-list {
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin: 1rem 0;
        }
        
        .place-tag {
            background: rgba(59, 130, 246, 0.2);
            border: 1px solid rgba(59, 130, 246, 0.4);
            border-radius: 40px;
            padding: 0.3rem 1rem;
            font-size: 0.8rem;
            transition: all 0.2s;
        }
        
        .place-tag:hover {
            background: rgba(59, 130, 246, 0.4);
        }
        
        .explore-btn {
            background: linear-gradient(135deg, #2c7da0, #1f5e7e);
            border: none;
            border-radius: 2rem;
            padding: 0.7rem 1.2rem;
            color: white;
            font-weight: 600;
            cursor: pointer;
            width: 100%;
            margin-top: 0.8rem;
            transition: all 0.3s;
        }
        
        .explore-btn:hover {
            background: linear-gradient(135deg, #3a8db0, #2a6e8e);
            transform: scale(0.98);
        }

        /* Modal */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.95);
            backdrop-filter: blur(15px);
            z-index: 1000;
            justify-content: center;
            align-items: center;
            animation: fadeIn 0.3s;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        .modal-content {
            background: linear-gradient(135deg, #0f1a2f, #0a1225);
            border-radius: 2rem;
            max-width: 850px;
            width: 90%;
            max-height: 85vh;
            overflow-y: auto;
            border: 1px solid rgba(59,130,246,0.5);
            box-shadow: 0 25px 50px rgba(0,0,0,0.5);
            animation: slideUp 0.4s;
        }
        
        @keyframes slideUp {
            from { transform: translateY(50px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        
        .modal-header {
            position: relative;
        }
        
        .modal-header img {
            width: 100%;
            height: 280px;
            object-fit: cover;
        }
        
        .close-modal {
            position: absolute;
            top: 15px;
            right: 20px;
            background: rgba(0,0,0,0.7);
            color: white;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }
        
        .close-modal:hover {
            background: #ff4757;
            transform: rotate(90deg);
        }
        
        .modal-body {
            padding: 2rem;
        }
        
        .modal-body h2 {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }
        
        .modal-info {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 1.2rem 0;
            background: rgba(0,0,0,0.3);
            padding: 1rem;
            border-radius: 1rem;
        }
        
        .info-item {
            display: flex;
            align-items: center;
            gap: 0.8rem;
        }
        
        .info-item i {
            font-size: 1.3rem;
            color: #4a9eff;
        }
        
        .cuisine-list {
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin-top: 0.5rem;
        }
        
        .cuisine-tag {
            background: rgba(74,158,255,0.2);
            border-radius: 40px;
            padding: 0.3rem 1rem;
            font-size: 0.85rem;
        }
        
        .fun-fact {
            background: linear-gradient(135deg, rgba(74,158,255,0.2), rgba(124,58,237,0.2));
            border-radius: 1rem;
            padding: 1rem;
            margin-top: 1rem;
            border-left: 3px solid #4a9eff;
        }

        footer {
            margin-top: 3rem;
            text-align: center;
            padding: 1.5rem;
            border-top: 1px solid rgba(255,255,255,0.1);
            font-size: 0.85rem;
            color: #8fadcc;
        }
        
        @media (max-width: 768px) {
            .main-wrapper { padding: 1rem; }
            .carousel-slide img { height: 300px; }
            .carousel-caption h3 { font-size: 1.2rem; }
            .country-showcase { grid-template-columns: 1fr; }
            .search-input { width: 180px; }
            .hero-stats { flex-direction: column; }
            #world-map { height: 350px; }
        }
        
        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #1a1a2e;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #4a9eff;
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #2c7da0;
        }
    </style>
</head>
<body>
<div class="bg-image"></div>
<div class="animated-overlay"></div>
<div class="main-wrapper">
    <div class="glass-header">
        <div class="logo"><i class="fas fa-globe-americas"></i> GlobeTrotter Elite</div>
        <form class="search-form" method="GET" action="/search" id="searchForm">
            <input type="text" name="q" class="search-input" placeholder="Search country, region or capital..." id="searchInput" value="{{ request.args.get('q', '') }}">
            <button class="search-btn" type="submit"><i class="fas fa-search"></i> Explore</button>
        </form>
        <div class="nav-links">
            <a href="/">Home</a>
            <a href="#destinations">Destinations</a>
            <a href="#world-map">World Map</a>
            <a href="#insights">Insights</a>
        </div>
    </div>

    <!-- Stats Section -->
    <div class="hero-stats">
        {% for stat in travel_stats %}
        <div class="stat-card">
            <i class="{{ stat.icon }}"></i>
            <div class="stat-value">{{ stat.value }}</div>
            <div class="stat-label">{{ stat.label }}</div>
        </div>
        {% endfor %}
    </div>

  

    <!-- Carousel Slider -->
    <div class="carousel-container" id="carousel">
        <div class="carousel-slides" id="carouselSlides">
            {% for img in carousel_images %}
            <div class="carousel-slide">
                <img src="{{ img.url }}" alt="{{ img.caption }}" loading="eager">
                <div class="carousel-caption">
                    <h3>{{ img.caption }}</h3>
                    <p>{{ img.description }}</p>
                </div>
            </div>
            {% endfor %}
        </div>
        <button class="carousel-btn carousel-prev" onclick="prevSlide()">❮</button>
        <button class="carousel-btn carousel-next" onclick="nextSlide()">❯</button>
        <div class="carousel-dots" id="carouselDots"></div>
    </div>

    <!-- Countries Section -->
    <div class="section-title" id="destinations">
        <i class="fas fa-map-marked-alt"></i> 
        <span>Top Destinations & Best Places</span>
        <span style="font-size: 0.9rem; background: rgba(74,158,255,0.2); padding: 0.2rem 0.8rem; border-radius: 20px;">Most Visited: France 🇫🇷</span>
    </div>
    <div class="country-showcase">
        {% for country in countries %}
        <div class="country-card" onclick="openCountryModal('{{ country.name }}')">
            <img src="{{ country.thumbnail }}" alt="{{ country.name }}">
            <div class="card-content">
                <div class="card-header">
                    <div class="country-name">
                        <i class="fas fa-flag-checkered"></i> {{ country.name }}
                        {% if country.most_visited %}
                        <span class="most-badge"><i class="fas fa-crown"></i> MOST VISITED</span>
                        {% endif %}
                    </div>
                    <div class="rank-badge">#{{ country.rank }}</div>
                </div>
                <div class="places-list">
                    {% for place in country.best_places[:4] %}
                    <span class="place-tag"><i class="fas fa-location-dot"></i> {{ place }}</span>
                    {% endfor %}
                </div>
                <button class="explore-btn" onclick="event.stopPropagation(); openCountryModal('{{ country.name }}')">
                    <i class="fas fa-compass"></i> Explore {{ country.name }}
                </button>
            </div>
        </div>
        {% endfor %}
    </div>
    
      <!-- 3D Interactive World Map -->
    <div class="world-map-container" id="world-map-section">
        <div class="map-header">
            <h3><i class="fas fa-map"></i> Explore World Map | Interactive 3D Globe</h3>
        </div>
        <div id="world-map"></div>
        <div class="map-controls">
            <button onclick="resetMapView()"><i class="fas fa-globe"></i> Reset View</button>
            <button onclick="zoomIn()"><i class="fas fa-search-plus"></i> Zoom In</button>
            <button onclick="zoomOut()"><i class="fas fa-search-minus"></i> Zoom Out</button>
        </div>
    </div>

    <!-- Travel Tips Section -->
    <div class="section-title" id="travel-tips">
        <i class="fas fa-lightbulb"></i>
        <span>Pro Travel Tips</span>
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.2rem; margin-bottom: 2rem;">
        <div style="background: rgba(74,158,255,0.1); border-radius: 1rem; padding: 1.2rem; border: 1px solid rgba(74,158,255,0.3);">
            <i class="fas fa-passport" style="font-size: 1.5rem; color: #4a9eff;"></i>
            <h3 style="margin: 0.5rem 0;">Visa & Documents</h3>
            <p style="font-size: 0.9rem;">Check visa requirements 3 months before travel. Many European countries require Schengen visa.</p>
        </div>
        <div style="background: rgba(74,158,255,0.1); border-radius: 1rem; padding: 1.2rem; border: 1px solid rgba(74,158,255,0.3);">
            <i class="fas fa-shield-alt" style="font-size: 1.5rem; color: #4a9eff;"></i>
            <h3 style="margin: 0.5rem 0;">Travel Insurance</h3>
            <p style="font-size: 0.9rem;">Always get comprehensive travel insurance covering medical emergencies and trip cancellation.</p>
        </div>
        <div style="background: rgba(74,158,255,0.1); border-radius: 1rem; padding: 1.2rem; border: 1px solid rgba(74,158,255,0.3);">
            <i class="fas fa-money-bill-wave" style="font-size: 1.5rem; color: #4a9eff;"></i>
            <h3 style="margin: 0.5rem 0;">Local Currency</h3>
            <p style="font-size: 0.9rem;">Carry local currency for small purchases. Notify your bank before international travel.</p>
        </div>
    </div>

    <!-- Recommendations Section -->
    <div class="section-title" id="insights">
        <i class="fas fa-star"></i>
        <span>Traveler's Choice Awards</span>
    </div>
    <div style="background: linear-gradient(135deg, rgba(15,35,65,0.6), rgba(10,20,40,0.6)); border-radius: 1.5rem; padding: 1.8rem; margin-bottom: 1rem;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.2rem;">
            <div><i class="fas fa-wine-bottle" style="color: #fbbf24;"></i> <strong>France:</strong> Wine tasting in Bordeaux & Champagne region</div>
            <div><i class="fas fa-palette" style="color: #fbbf24;"></i> <strong>Spain:</strong> Gaudí's Sagrada Familia & flamenco shows</div>
            <div><i class="fas fa-gondola" style="color: #fbbf24;"></i> <strong>Italy:</strong> Gondola ride in Venice & authentic pizza in Naples</div>
            <div><i class="fas fa-mountain" style="color: #fbbf24;"></i> <strong>Japan:</strong> Mount Fuji & cherry blossom season (Sakura)</div>
            <div><i class="fas fa-fish" style="color: #fbbf24;"></i> <strong>Australia:</strong> Great Barrier Reef snorkeling & Sydney Harbour cruise</div>
            <div><i class="fas fa-umbrella-beach" style="color: #fbbf24;"></i> <strong>Thailand:</strong> Island hopping in Phuket & Krabi</div>
            <div><i class="fas fa-landmark" style="color: #fbbf24;"></i> <strong>Greece:</strong> Santorini sunsets & ancient Athens exploration</div>
            <div><i class="fas fa-futbol" style="color: #fbbf24;"></i> <strong>Brazil:</strong> Rio Carnival & Amazon jungle adventures</div>
        </div>
    </div>
    
    <footer>
        <i class="fas fa-plane-departure"></i> 2026 GlobeTrotter Elite — Your Journey Starts Here<br>
        <span style="font-size: 0.75rem;">Based on UNESCO World Heritage sites, travel statistics, and global tourism rankings | 8 Amazing Destinations Featured</span>
    </footer>
</div>

<!-- Modal -->
<div id="countryModal" class="modal">
    <div class="modal-content" id="modalContent">
        <!-- Dynamic content loaded via JavaScript -->
    </div>
</div>

<!-- Three.js and Map Libraries -->
<script type="importmap">
    {
        "imports": {
            "three": "https://unpkg.com/three@0.128.0/build/three.module.js"
        }
    }
</script>

<script type="module">
    import * as THREE from 'three';
    import { OrbitControls } from 'https://unpkg.com/three@0.128.0/examples/jsm/controls/OrbitControls.js';
    
    // Setup 3D World Map
    const container = document.getElementById('world-map');
    const width = container.clientWidth;
    const height = container.clientHeight;
    
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x050b1a);
    scene.fog = new THREE.FogExp2(0x050b1a, 0.0008);
    
    const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    camera.position.set(0, 0, 3.5);
    
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(width, height);
    renderer.setPixelRatio(window.devicePixelRatio);
    container.appendChild(renderer.domElement);
    
    // Controls for interactivity
    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.autoRotate = true;
    controls.autoRotateSpeed = 0.8;
    controls.enableZoom = true;
    controls.enablePan = false;
    controls.zoomSpeed = 1.2;
    controls.rotateSpeed = 1.0;
    
    // Load Earth texture
    const textureLoader = new THREE.TextureLoader();
    const earthMap = textureLoader.load('https://threejs.org/examples/textures/planets/earth_atmos_2048.jpg');
    const earthSpecularMap = textureLoader.load('https://threejs.org/examples/textures/planets/earth_specular_2048.jpg');
    const earthNormalMap = textureLoader.load('https://threejs.org/examples/textures/planets/earth_normal_2048.jpg');
    const cloudMap = textureLoader.load('https://threejs.org/examples/textures/planets/earth_clouds_1024.png');
    
    // Earth sphere
    const earthGeometry = new THREE.SphereGeometry(1.2, 128, 128);
    const earthMaterial = new THREE.MeshPhongMaterial({
        map: earthMap,
        specularMap: earthSpecularMap,
        specular: new THREE.Color('grey'),
        shininess: 5,
        normalMap: earthNormalMap,
        normalScale: new THREE.Vector2(0.8, 0.8)
    });
    const earth = new THREE.Mesh(earthGeometry, earthMaterial);
    scene.add(earth);
    
    // Clouds layer
    const cloudGeometry = new THREE.SphereGeometry(1.21, 128, 128);
    const cloudMaterial = new THREE.MeshPhongMaterial({
        map: cloudMap,
        transparent: true,
        opacity: 0.15,
        blending: THREE.AdditiveBlending
    });
    const clouds = new THREE.Mesh(cloudGeometry, cloudMaterial);
    scene.add(clouds);
    
    // Stars background
    const starGeometry = new THREE.BufferGeometry();
    const starCount = 2500;
    const starPositions = new Float32Array(starCount * 3);
    for (let i = 0; i < starCount; i++) {
        starPositions[i*3] = (Math.random() - 0.5) * 2000;
        starPositions[i*3+1] = (Math.random() - 0.5) * 1000;
        starPositions[i*3+2] = (Math.random() - 0.5) * 200 - 80;
    }
    starGeometry.setAttribute('position', new THREE.BufferAttribute(starPositions, 3));
    const starMaterial = new THREE.PointsMaterial({ color: 0xffffff, size: 0.25, transparent: true, opacity: 0.8 });
    const stars = new THREE.Points(starGeometry, starMaterial);
    scene.add(stars);
    
    // Lighting
    const ambientLight = new THREE.AmbientLight(0x333333);
    scene.add(ambientLight);
    const directionalLight = new THREE.DirectionalLight(0xffffff, 1.2);
    directionalLight.position.set(5, 3, 5);
    scene.add(directionalLight);
    const backLight = new THREE.PointLight(0x4466cc, 0.5);
    backLight.position.set(-2, -1, -3);
    scene.add(backLight);
    const fillLight = new THREE.PointLight(0x88aaff, 0.3);
    fillLight.position.set(1, 2, 2);
    scene.add(fillLight);
    
    // Animation loop
    function animate() {
        requestAnimationFrame(animate);
        controls.update();
        renderer.render(scene, camera);
    }
    animate();
    
    // Handle window resize
    window.addEventListener('resize', () => {
        const newWidth = container.clientWidth;
        const newHeight = container.clientHeight;
        camera.aspect = newWidth / newHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(newWidth, newHeight);
    });
    
    // Expose controls to global for map control buttons
    window.resetMapView = () => {
        camera.position.set(0, 0, 3.5);
        controls.target.set(0, 0, 0);
        controls.update();
    };
    
    window.zoomIn = () => {
        camera.position.z *= 0.9;
        controls.update();
    };
    
    window.zoomOut = () => {
        camera.position.z *= 1.1;
        controls.update();
    };
</script>

<script>
    // Carousel functionality
    let currentSlide = 0;
    const slides = document.querySelectorAll('.carousel-slide');
    const totalSlides = slides.length;
    const slidesContainer = document.getElementById('carouselSlides');
    
    function updateCarousel() {
        if (slidesContainer) {
            slidesContainer.style.transform = `translateX(-${currentSlide * 100}%)`;
            const dots = document.querySelectorAll('.dot');
            dots.forEach((dot, i) => {
                dot.classList.toggle('active', i === currentSlide);
            });
        }
    }
    
    function nextSlide() {
        currentSlide = (currentSlide + 1) % totalSlides;
        updateCarousel();
    }
    
    function prevSlide() {
        currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
        updateCarousel();
    }
    
    // Create dots if carousel exists
    const dotsContainer = document.getElementById('carouselDots');
    if (dotsContainer && slides.length > 0) {
        for (let i = 0; i < totalSlides; i++) {
            const dot = document.createElement('div');
            dot.classList.add('dot');
            if (i === 0) dot.classList.add('active');
            dot.onclick = (function(index) {
                return function() {
                    currentSlide = index;
                    updateCarousel();
                };
            })(i);
            dotsContainer.appendChild(dot);
        }
    }
    
    // Auto slide every 5 seconds
    let autoSlide = setInterval(() => {
        if (document.getElementById('carousel')) {
            nextSlide();
        }
    }, 5000);
    
    const carouselElement = document.getElementById('carousel');
    if (carouselElement) {
        carouselElement.addEventListener('mouseenter', () => clearInterval(autoSlide));
        carouselElement.addEventListener('mouseleave', () => {
            autoSlide = setInterval(nextSlide, 5000);
        });
    }
    
    // Country data from backend
    const countriesData = {{ countries | tojson }};
    
    function openCountryModal(countryName) {
        const country = countriesData.find(c => c.name === countryName);
        if (!country) return;
        
        const modal = document.getElementById('countryModal');
        const modalContent = document.getElementById('modalContent');
        
        modalContent.innerHTML = `
            <div class="modal-header">
                <img src="${country.image}" alt="${country.name}">
                <button class="close-modal" onclick="closeModal()">×</button>
            </div>
            <div class="modal-body">
                <h2><i class="fas fa-flag-checkered"></i> ${country.name}</h2>
                <div class="modal-info">
                    <div class="info-item"><i class="fas fa-calendar-alt"></i> <strong>Best Time:</strong> ${country.best_time || 'Year-round'}</div>
                    <div class="info-item"><i class="fas fa-money-bill-wave"></i> <strong>Currency:</strong> ${country.currency || 'Varies'}</div>
                    <div class="info-item"><i class="fas fa-language"></i> <strong>Language:</strong> ${country.language || 'Multiple'}</div>
                    <div class="info-item"><i class="fas fa-trophy"></i> <strong>Global Rank:</strong> #${country.rank}</div>
                    <div class="info-item"><i class="fas fa-plane"></i> <strong>Main Airport:</strong> ${country.airport || 'Multiple airports'}</div>
                    <div class="info-item"><i class="fas fa-heart"></i> <strong>Famous For:</strong> ${country.famous_for || 'Culture & Tourism'}</div>
                </div>
                <p style="line-height: 1.6; margin: 1rem 0;">${country.description}</p>
                <div class="fun-fact">
                    <i class="fas fa-lightbulb" style="color: #fbbf24;"></i> <strong>Did you know?</strong> ${country.fun_fact}
                </div>
                <h3 style="margin-top: 1.2rem;"><i class="fas fa-utensils"></i> Must-Try Cuisine</h3>
                <div class="cuisine-list">
                    ${country.cuisine.map(c => `<span class="cuisine-tag">${c}</span>`).join('')}
                </div>
                <h3 style="margin-top: 1.2rem;"><i class="fas fa-map-marker-alt"></i> Top Places to Visit</h3>
                <div class="cuisine-list">
                    ${country.best_places.map(p => `<span class="cuisine-tag"><i class="fas fa-location-dot"></i> ${p}</span>`).join('')}
                </div>
                <button class="explore-btn" style="margin-top: 1.5rem;" onclick="closeModal()">
                    <i class="fas fa-times"></i> Close
                </button>
            </div>
        `;
        
        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden';
    }
    
    function closeModal() {
        const modal = document.getElementById('countryModal');
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
    
    // Close modal on outside click
    window.onclick = function(event) {
        const modal = document.getElementById('countryModal');
        if (event.target === modal) {
            closeModal();
        }
    }
</script>
</body>
</html>
'''

@app.route('/')
@app.route('/home')
def home():
    return render_template_string(HTML_TEMPLATE, countries=countries_data, carousel_images=carousel_images, travel_stats=travel_stats)

@app.route('/search')
def search():
    q = request.args.get('q', '').strip().lower()
    matches = []
    if q:
        matches = [c for c in country_search_data if q in c['name'].lower() or q in c['region'].lower() or q in c['capital'].lower()]
    
    if not matches and q:
        suggestions = [c['name'] for c in country_search_data[:5]]
        result_html = f"""
        <div style="text-align: center; padding: 2rem;">
            <i class="fas fa-search" style="font-size: 4rem; color: #4a9eff;"></i>
            <h3 style="margin: 1rem 0;">No results found for "{q}"</h3>
            <p>Try searching for: {', '.join(suggestions)}</p>
            <button onclick="window.location.href='/'" style="background: linear-gradient(135deg, #2c7da0, #1f5e7e); border: none; padding: 0.7rem 1.5rem; border-radius: 2rem; color: white; cursor: pointer; margin-top: 1rem;">Back to Home</button>
        </div>
        """
    elif not q:
        result_html = "<div style='text-align: center; padding: 2rem;'><i class='fas fa-search' style='font-size: 4rem;'></i><h3>Enter a country name to search</h3><button onclick=\"window.location.href='/'\" style='background: linear-gradient(135deg, #2c7da0, #1f5e7e); border: none; padding: 0.7rem 1.5rem; border-radius: 2rem; color: white; cursor: pointer; margin-top: 1rem;'>Back to Home</button></div>"
    else:
        rows = ''.join(f"""
        <div style="background: rgba(18,28,50,0.9); border-radius: 1rem; padding: 1rem; margin-bottom: 1rem; display: flex; gap: 1rem; align-items: center; flex-wrap: wrap; border: 1px solid rgba(74,158,255,0.3);">
            <img src="{c['image']}" style="width: 100px; height: 80px; object-fit: cover; border-radius: 0.8rem;">
            <div style="flex: 1;">
                <h3><i class="fas fa-globe"></i> {c['name']}</h3>
                <p><i class="fas fa-map-marker-alt"></i> {c['region']} | <i class="fas fa-city"></i> {c['capital']} | <i class="fas fa-users"></i> Population: {c['population']}<br>
                <i class="fas fa-language"></i> {c['language']} | <i class="fas fa-money-bill"></i> {c['currency']}</p>
            </div>
            <button onclick="window.location.href='/'" style="background: linear-gradient(135deg, #2c7da0, #1f5e7e); border: none; padding: 0.5rem 1rem; border-radius: 2rem; color: white; cursor: pointer;">Home</button>
        </div>
        """ for c in matches)
        result_html = f"<h3 style='margin-bottom: 1.5rem; color: #4a9eff;'>✨ Found {len(matches)} amazing result(s) for '{q}':</h3>{rows}"
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Search Results | GlobeTrotter Elite</title>
        <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                background: linear-gradient(135deg, #0a0a1a, #0f0f1f);
                font-family: 'Plus Jakarta Sans', sans-serif;
                color: #eef2ff;
                min-height: 100vh;
            }}
            .container {{
                max-width: 900px;
                margin: 0 auto;
                padding: 2rem;
            }}
            .back-home {{
                display: inline-flex;
                align-items: center;
                gap: 8px;
                background: linear-gradient(135deg, #2c7da0, #1f5e7e);
                padding: 0.7rem 1.5rem;
                border-radius: 2rem;
                color: white;
                text-decoration: none;
                margin-bottom: 2rem;
                transition: all 0.3s;
            }}
            .back-home:hover {{
                transform: translateX(-5px);
                box-shadow: 0 5px 15px rgba(44,125,160,0.4);
            }}
            h1 {{
                font-size: 2rem;
                margin-bottom: 1.5rem;
                background: linear-gradient(135deg, #fff, #4a9eff);
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <a href="/" class="back-home"><i class="fas fa-arrow-left"></i> Back to Dashboard</a>
            <h1><i class="fas fa-search"></i> Search Results</h1>
            {result_html}
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)