# charm-prometheus-slurm-exporter

## Quickstart
```bash
juju deploy slurm-core
juju deploy prometheus-slurm-exporter
juju relate slurmctld:juju-info prometheus-slurm-exporter

juju deploy prometheus2

juju relate prometheus2 prometheus-slurm-exporter
```

## Development
```bash
git clone git@github.com:omnivector-solutions/charm-prometheus-slurm-exporter && \
    cd charm-prometheus-slurm-exporter
charmcraft build
juju deploy ./prometheus-slurm-exporter.charm \
    --resource prometheus-slurm-exporter=/path/to/prometheus-slurm-exporter.snap
```

#### Copyright
* Omnivector Solutions (c) 2020

#### License
* MIT - see `LICENSE` file in this directory
