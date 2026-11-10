ENV ?= integration
install:
	pip install -r requirements.txt
	rfbrowser init
test:
	robot --variablefile config/environments/$(ENV).py --outputdir results tests
report:
	python scripts/metrics.py results/output.xml results/metrics.json
	python scripts/dashboard.py results/metrics.json results/dashboard.html
gate:
	python scripts/quality_gate.py results/metrics.json
