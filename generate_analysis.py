import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def generate_evidence():
    print("📊 Loading dataset for analysis...")
    
    # Check if data exists
    data_path = 'data/creditcard.csv'
    if not os.path.exists(data_path):
        print(f"❌ Error: {data_path} not found.")
        return

    # Load Data
    df = pd.read_csv(data_path)
    
    # Calculate Correlation with 'Class' (Target)
    print("🧮 Calculating correlations...")
    correlations = df.corrwith(df['Class']).sort_values()
    
    # Remove 'Class' from the graph (it correlates 100% with itself)
    correlations = correlations.drop('Class')

    # --- PLOT 1: Feature Importance Bar Chart ---
    plt.figure(figsize=(12, 10))
    
    # Color logic: Red for strong negative correlation (Fraud indicators like V14, V17)
    # Blue for positive, Gray for weak.
    colors = []
    for x in correlations:
        if x < -0.15: colors.append('#ff4d4d') # Strong Negative (Red)
        elif x > 0.15: colors.append('#00c6ff') # Strong Positive (Blue)
        else: colors.append('#cccccc') # Weak (Gray)

    correlations.plot(kind='barh', color=colors)
    
    plt.title("Scientific Evidence: Key Features Correlated with Fraud", fontsize=16, fontweight='bold')
    plt.xlabel("Correlation Strength (Negative = Low Value implies Fraud)", fontsize=12)
    plt.ylabel("Feature Name", fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    
    # Save the plot
    output_file = 'feature_importance_proof.png'
    plt.tight_layout()
    plt.savefig(output_file)
    print(f"✅ Success! Evidence graph saved as '{output_file}'")
    print("   -> Include this image in your presentation to prove V14/V17 importance.")
    plt.show()

if __name__ == "__main__":
    generate_evidence()