# charm-prometheus-node-exporter

## Quickstart
```bash
juju deploy slurm-core
juju deploy prometheus-node-exporter
juju relate slurmctld:juju-info prometheus-node-exporter

juju deploy prometheus2

juju relate prometheus2 prometheus-node-exporter
```

## Development
```bash
git clone git@github.com:omnivector-solutions/charm-prometheus-node-exporter && \
    cd charm-prometheus-node-exporter
charmcraft build
juju deploy ./prometheus-node-exporter.charm \
    --resource prometheus-node-exporter=/path/to/prometheus-node-exporter.snap
```

#### Copyright
* Omnivector Solutions (c) 2020

#### License
* MIT - see `LICENSE` file in this directory
