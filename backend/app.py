from flask import Flask, render_template
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

# ====================== CITIZEN VIEW ======================
@app.route('/citizen')
def citizen_view():
    return render_template('citizen.html', 
                           points=125,
                           badges=["Eco Hero", "Green Champion", "Bin Master"],
                           message="Thank you! You helped save 4.8 kg CO₂ today!")

# ====================== RECYCLER VIEW ======================
@app.route('/recycler')
def recycler_view():
    return render_template('recycler.html',
                           stock={"Smartphones": 18, "Laptops": 7, "Cables": 45},
                           value=1240.50)

# ====================== REGULATOR VIEW ======================
@app.route('/regulator')
def regulator_view():
    return render_template('regulator.html',
                           total_bins=12,
                           recycling_rate=68.4,
                           co2_saved=124.8,
                           compliance="100% - Basel & EPR compliant")

# ====================== HOME PAGE ======================
@app.route('/')
def home():
    return '''
    <h1>SEMIS Smart E-Waste Dashboard</h1>
    <p><a href="/citizen">👤 Citizen View</a> | 
       <a href="/recycler">♻️ Recycler View</a> | 
       <a href="/regulator">📋 Regulator View</a></p>
    <p><strong>Live prototype ready for dissertation demonstration!</strong></p>
    '''

if __name__ == '__main__':
    print("🚀 SEMIS Dashboard running at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
