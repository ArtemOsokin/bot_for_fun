CODE = bot
BLACK = black --line-length 100 --target-version py310 --skip-string-normalization

format:
	isort $(CODE)
	${BLACK} $(CODE)

run:
	python3 run.py
