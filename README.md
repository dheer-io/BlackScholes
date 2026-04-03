# Black-Scholes Quant Dashboard 📊

An interactive options pricing dashboard built using the Black-Scholes model.  
This application enables real-time exploration of option pricing, Greeks, and profit & loss (P&L) under varying market conditions.

🔗 **Live Demo:**  
https://blackschole.streamlit.app/

---

## 🚀 Features

### 📈 Option Pricing
- Computes European Call and Put option prices using the Black-Scholes model
- Accurate and efficient implementation of core pricing equations

### 📊 Greeks Dashboard
- Delta, Gamma, Vega, Theta
- Helps analyze sensitivity to:
  - Underlying price
  - Volatility
  - Time decay

### 💰 P&L Analysis (Key Feature)
- Input custom purchase price for Call and Put options
- Visualize actual profit/loss instead of just theoretical values
- Useful for understanding real trading outcomes

### 🔥 Interactive Heatmaps
- Explore how option price and P&L change with:
  - Spot Price
  - Volatility
- Color-coded visualization:
  - 🟢 Green → Profit
  - 🔴 Red → Loss
  - ⚪ Neutral → Break-even

### 🎛️ Real-time Parameter Control
- Adjust:
  - Spot Price
  - Strike Price
  - Volatility
  - Time to Maturity
  - Risk-Free Interest Rate
- Instant recalculation and visualization

---

## 📸 Demo

### Pricing & Greeks Dashboard
![Dashboard](screenshot1.png)

### P&L Heatmaps
![Heatmap](screenshot2.png)

---

## ⚙️ Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/quant-dashboard.git
cd quant-dashboard
pip install -r requirements.txt
streamlit run app.py
```

---

## 📂 Project Structure

```
.
├── app.py
├── black_scholes.py
├── requirements.txt
├── README.md
```

---

## 🧠 Motivation

This project bridges quantitative finance theory with practical trading intuition.

Instead of only computing theoretical option prices, it enables:
- P&L visualization across market scenarios
- Sensitivity analysis using Greeks
- Interactive exploration of option behavior

---

## 🔮 Future Improvements

- Implied Volatility Solver
- Options Strategy Builder (Straddle, Strangle)
- 3D Surface Visualization

---

## 📌 Tech Stack

- Python
- Streamlit
- NumPy
- SciPy
- Plotly
