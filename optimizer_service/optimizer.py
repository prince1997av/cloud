import yaml
import psutil
import time
import logging

# Configura logging
logging.basicConfig(filename='/var/log/resource_optimizer/optimizer.log', level=logging.INFO)

def load_config(config_path):
    with open(config_path, 'r') as config_file:
        return yaml.safe_load(config_file)

def optimize_resources(config):
    logging.info("Starting resource optimization...")
    while True:
        # Analisi delle risorse del sistema
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()

        logging.info(f"CPU Usage: {cpu_usage}%, Memory Usage: {memory.percent}%")
        
        # Logica di ottimizzazione (esempio: notifiche o resizing)
        if cpu_usage > config['thresholds']['cpu']:
            logging.warning("High CPU usage detected! Consider resizing the VM.")
        if memory.percent > config['thresholds']['memory']:
            logging.warning("High memory usage detected! Consider resizing the VM.")
        
        time.sleep(config['scan_interval'])

if __name__ == "__main__":
    config = load_config("/etc/resource_optimizer/config.yaml")
    optimize_resources(config)

