# Del 3 – Integrationstester

## Syfte
Syftet med detta projekt är att verifiera att externa API:er fungerar som förväntat genom integrationstester, samt att säkerställa att testerna körs automatiskt via GitHub Actions.

## API:er som testas
- [FakeStore API](https://fakestoreapi.com) – används för lokala tester
- [DummyJSON API](https://dummyjson.com) – används för CI/CD-tester i GitHub Actions

## Verktyg
- Python
- Pytest
- Requests
- GitHub Actions

## Struktur
```bash
├── Del_3_fakestore_tests.py         # Tester mot FakeStore API
├── Del_3_test_dummyjson.py          # Tester mot DummyJSON API
├── requirements.txt                 # Beroenden
└── .github/
    └── workflows/
        └── tests.yml                # CI-konfiguration
