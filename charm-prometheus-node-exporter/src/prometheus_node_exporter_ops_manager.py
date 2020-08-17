#!/usr/bin/python3
"""PrometheusNodeExporterManager."""
import subprocess
import sys


class PrometheusNodeExporterManager:
    """PrometheusNodeExporterManager."""

    def __init__(self):
        """Init class attributes."""
        self.name = 'PrometheusNodeExporterManager'

    def install(self, resource_path):
        """Install the prometheus-node-exporter snap."""
        try:
            subprocess.call([
                "snap",
                "install",
                resource_path,
                "--dangerous",
                "--classic",
            ])
        except subprocess.CalledProcessError as e:
            print(f"Cannot install prometheus-node-exporter - {e}")
            sys.exit(-1)
