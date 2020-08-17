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
from prometheus_node_exporter import (
    PrometheusNodeExporterProvides,
)
from prometheus_node_exporter_ops_manager import (
    PrometheusNodeExporterManager,
)


class PrometheusNodeExporterCharm(CharmBase):
    """PrometheusNodeExporterCharm."""

    _stored = StoredState()

    def __init__(self, *args):
        """Initialize charm."""
        super().__init__(*args)

        self._stored.set_default(
            prometheus_node_exporter_installed=False,
        )

        self.prometheus_node_exporter = PrometheusNodeExporterProvides(
            self,
            "prometheus"
        )

        self.framework.observe(self.on.install, self._on_install)

    def _on_install(self, event):
        try:
            prometheus_node_exporter_resource_path = \
                self.model.resources.fetch('prometheus-node-exporter')
        except ModelError as e:
            print(f"Cannot find resource - {e}")
            prometheus_node_exporter_resource_path = None

        if prometheus_node_exporter_resource_path is not None:
            PrometheusNodeExporterManager().install(
                prometheus_node_exporter_resource_path
            )
            self._stored.prometheus_node_exporter_installed = True
            self.unit.status = ActiveStatus("Node exporter installed")
        else:
            self.unit.status = BlockedStatus(
                "No prometheus-node-exporter snap resource found"
            )
            event.defer()

    def is_prometheus_node_exporter_installed(self):
        """Return True/False based on whether the exporter is install."""
        return self._stored.prometheus_node_exporter_installed


if __name__ == "__main__":
    main(PrometheusNodeExporterCharm)
