run_server:
	uvicorn main:app --reload

run_stress_test:
	ab -n 800 -c 10 http://127.0.0.1:8000/ping/

build_container:
	docker compose up --build
build_container_detach:
	docker compose up -d --build
down_container_with_volume:
	docker compose down -v
down_container_without_volume:
	docker compose down

get_api:
	docker exec -it api /bin/bash
get_redis:
	docker exec -it redis sh

.PHONY: run_server
.PHONY: run_stress_test
.PHONY: build_container, build_container_detach,down_container_with_volume,down_container_without_volume
.PHONY: get_api.get_redis
