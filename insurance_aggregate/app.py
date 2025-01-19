from flask import Flask, render_template, request
from data_ingestion import load_data
from data_normalisation import normalise_data
from data_aggregation import aggregate_data
from reporting import calculate_metrics, filter_by_broker

app = Flask(__name__)

# Load and normalize data
broker1 = normalise_data(load_data('data/broker1.csv'), 'broker1')
broker2 = normalise_data(load_data('data/broker2.csv'), 'broker2')

# Add broker identifiers
broker1['broker'] = 'broker1'
broker2['broker'] = 'broker2'

# Aggregate all data
aggregated_data = aggregate_data([broker1, broker2])

@app.route('/')
def index():
    """Render the index page."""
    return render_template('index.html')

@app.route('/report', methods=['POST'])
def report():
    """Generate the insurance policy report based on user input."""
    metrics = calculate_metrics(aggregated_data)
    broker_name = request.form.get('broker_name')

    # Filter data by broker if broker name is provided
    filtered_data = filter_by_broker(aggregated_data, broker_name) if broker_name else aggregated_data

    # Avoid SettingWithCopyWarning by creating a copy before modifying
    filtered_data = filtered_data.copy()

    # Format date columns for display
    if 'start_date' in filtered_data.columns:
        filtered_data['start_date'] = filtered_data['start_date'].dt.strftime('%Y-%m-%d')
    if 'end_date' in filtered_data.columns:
        filtered_data['end_date'] = filtered_data['end_date'].dt.strftime('%Y-%m-%d')

    # Convert filtered data to a dictionary format for rendering
    policies = filtered_data.to_dict(orient='records')

    return render_template('report.html', metrics=metrics, policies=policies)

if __name__ == "__main__":
    app.run(debug=True)
