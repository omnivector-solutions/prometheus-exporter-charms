#!/usr/bin/python3
"""PrometheusSlurmExporterManager."""
import subprocess
import sys


class PrometheusSlurmExporterManager:
    """PrometheusSlurmExporterManager."""

    def __init__(self):
        """Init class attributes."""
        self.name = 'PrometheusSlurmExporterManager'

    def install(self, resource_path):
        """Install the prometheus-slurm-exporter charm."""
        try:
            subprocess.call([
                "snap",
                "install",
                resource_path,
                "--dangerous",
                "--classic",
            ])
        except subprocess.CalledProcessError as e:
            print(f"Cannot install prometheus-slurm-exporter - {e}")
            sys.exit(-1)
