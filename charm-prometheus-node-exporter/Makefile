# TARGETS
lint: ## Run linter
	tox -e lint

clean: ## Remove .tox and build dirs
	rm -rf .tox/
	rm -rf venv/
	rm -rf build/

push-charm-to-edge: ## Push the charm to edge channel
	@aws s3 cp --acl public-read ./prometheus-node-exporter.charm s3://omnivector-public-assets/charms/prometheus-node-exporter

pull-charm-from-edge: ## Push the charm to edge channel
	@wget https://omnivector-public-assets.s3-us-west-2.amazonaws.com/charms/prometheus-node-exporter/prometheus-node-exporter.charm

pull-snap-from-edge: ## Pull the classic slurm snap from s3
	@wget https://omnivector-public-assets.s3-us-west-2.amazonaws.com/snaps/prometheus-node-exporter/edge/prometheus-node-exporter_1.0.1_amd64.snap -O prometheus-node-exporter.snap

# Display target comments in 'make help'
help: 
	grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# SETTINGS
# Use one shell for all commands in a target recipe
.ONESHELL:
# Set default goal
.DEFAULT_GOAL := help
# Use bash shell in Make instead of sh 
SHELL := /bin/bash
