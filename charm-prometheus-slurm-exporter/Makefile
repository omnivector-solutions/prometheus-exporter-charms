# TARGETS
lint: ## Run linter
	tox -e lint

clean: ## Remove .tox and build dirs
	rm -rf .tox/
	rm -rf venv/
	rm -rf build/


pull-slurm-prometheus-exporter-snap: ## Pull the classic slurm snap from github
	@wget https://omnivector-public-assets.s3-us-west-2.amazonaws.com/resources/prometheus-slurm-exporter/prometheus-slurm-exporter_0.11-1-g01dd959_amd64.snap -O prometheus-slurm-exporter.snap

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
