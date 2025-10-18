.PHONY: setup run plots clean

setup:
	python -m venv .venv && . .venv/bin/activate && pip install -U pip && pip install -r requirements.txt

run:
	. .venv/bin/activate && python -m src.simulate_fields --config configs/base.yaml && \
	python -m src.detect_patterns --config configs/base.yaml

plots:
	. .venv/bin/activate && python -m src.visualize --config configs/base.yaml

clean:
	rm -rf outputs/*
