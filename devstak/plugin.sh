# Funzione per l'installazione delle dipendenze del plugin
function plugin_install() {
    echo "Installing Resource Optimizer..."
    sudo apt-get update
    sudo apt-get install -y python3-yaml python3-psutil
}

# Configura il plugin
function plugin_configure() {
    echo "Configuring Resource Optimizer..."
    # Copia i file di configurazione del plugin
    cp $PLUGIN_DIR/optimizer_service/config.yaml /etc/resource_optimizer/config.yaml
    mkdir -p /var/log/resource_optimizer/
    touch /var/log/resource_optimizer/optimizer.log
}

# Avvio del servizio di ottimizzazione
function plugin_start() {
    echo "Starting Resource Optimizer service..."
    run_process resource-optimizer "python3 $PLUGIN_DIR/optimizer_service/optimizer.py --config /etc/resource_optimizer/config.yaml"
}

# Registra le fasi del plugin
if is_service_enabled resource-optimizer; then
    echo "Resource Optimizer is enabled."
    register_install_hook plugin_install
    register_configure_hook plugin_configure
    register_start_hook plugin_start
fi

