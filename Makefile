activate_virtual_environment:
	. env/bin/activate
deactivate_virtual_environment:
	deactivate
update_dependencies:
	pip freeze > requirements.txt

run_server:
	uvicorn main:app --reload

run_stress_test:
	ab -n 800 -c 10 http://127.0.0.1:8000/ping/

run_test_inside_container:
	docker-compose exec api python -m pytest -s .

create_summarie:
	http --json POST http://localhost:8004/summaries/ url=http://testdriven.io
clear_summaries:
	http --json DELETE http://localhost:8004/summaries/

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
get_api_db:
	docker exec -it api-db psql -U postgres
get_redis:
	docker exec -it redis sh
init_aerich:
	docker compose exec api aerich init -t database.config.TORTOISE_ORM
init_migration:
	docker-compose exec api aerich init-db
upgrade_migration:
	docker-compose exec api aerich upgrade

get_all_summaries_inside_container:
	docker exec -it api-db  psql -U postgres -d api_dev -c "SELECT * FROM textsummary"
delete_all_summaries_inside_container:
	docker exec -it api-db  psql -U postgres -d api_dev -c "TRUNCATE textsummary RESTART IDENTITY"


.PHONY: activate_virtual_environment,deactivate_virtual_environment,update_dependencies
.PHONY: run_server
.PHONY: run_stress_test
.PHONY: build_container, build_container_detach,down_container_with_volume,down_container_without_volume
.PHONY: get_api,get_redis,init_aerich,init_migration,upgrade_migration
.PHONY: run_test_inside_container
.PHONY: create_summarie
