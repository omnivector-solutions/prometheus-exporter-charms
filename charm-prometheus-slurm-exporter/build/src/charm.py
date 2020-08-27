#!/usr/bin/python3
"""SlurmctldCharm."""
from ops.charm import CharmBase
from ops.framework import StoredState
from ops.main import main
from ops.model import (
    ActiveStatus,
    BlockedStatus,
    ModelError,
)
from prometheus_slurm_exporter import (
    PrometheusSlurmExporterProvides,
)
from prometheus_slurm_exporter_ops_manager import (
    PrometheusSlurmExporterManager,
)


class PrometheusSlurmExporterCharm(CharmBase):
    """PrometheusSlurmExporterCharm."""

    _stored = StoredState()

    def __init__(self, *args):
        """Initialize charm."""
        super().__init__(*args)

        self._stored.set_default(
            prometheus_node_exporter_installed=False,
        )

        self.prometheus_slurm_exporter = PrometheusSlurmExporterProvides(
            self,
            "prometheus"
        )

        self.framework.observe(self.on.install, self._on_install)

    def _on_install(self, event):
        """Install the prometheus-slurm-exporter snap."""
        try:
            prometheus_slurm_exporter_resource_path = \
                self.model.resources.fetch('prometheus-slurm-exporter')
        except ModelError as e:
            print(f"Cannot find resource - {e}")
            prometheus_slurm_exporter_resource_path = None

        if prometheus_slurm_exporter_resource_path is not None:
            PrometheusSlurmExporterManager().install(
                prometheus_slurm_exporter_resource_path
            )
            self._stored.prometheus_node_exporter_installed = True
            self.unit.status = ActiveStatus("")
        else:
            self.unit.status = BlockedStatus(
                "No prometheus-slurm-exporter snap resource found"
            )
            event.defer()

    def is_prometheus_slurm_exporter_installed(self):
        """Return True/False based on whether the exporter is install."""
        return self._stored.prometheus_node_exporter_installed


if __name__ == "__main__":
    main(PrometheusSlurmExporterCharm)
