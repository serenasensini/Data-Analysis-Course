from app import create_app
def run_smoke_test() -> None:
    app = create_app()
    client = app.test_client()
    checks = [
        ("/health", 200),
        ("/api/oldestMovie", 301),
        ("/api/bestMovie", 301),
        ("/api/totMoviePerYear", 301),
    ]
    for endpoint, expected_status in checks:
        response = client.get(endpoint)
        assert response.status_code == expected_status, (
            f"Unexpected status for {endpoint}: "
            f"expected {expected_status}, got {response.status_code}"
        )
    print("Smoke test passed: all endpoints respond with expected status codes.")
if __name__ == "__main__":
    run_smoke_test()
