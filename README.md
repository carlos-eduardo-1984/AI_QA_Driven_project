# AI-Assisted Robot Framework Quality Pipeline

A complete GitHub project to retrieve Jira Cloud requirements by label, generate concise Gherkin scenarios with AI, submit them for manual approval, generate Robot Framework tests, and publish HTML dashboards and quality gates.

## Workflow
1. `requirements-to-gherkin.yml`: Jira label -> AI -> `features/pending` -> Pull Request for manual approval.
2. Approval is controlled through PR review/merge and the `gherkin-approval` GitHub Environment with Required Reviewers.
3. Approved content must be stored in `features/approved`.
4. `gherkin-to-robot.yml`: approved Gherkin -> AI -> Robot Framework tests -> technical Pull Request.
5. `robot-tests.yml`: executes Browser Library + RequestsLibrary tests against `integration` or `test`.
6. The pipeline generates `report.html`, `log.html`, `output.xml`, `metrics.json`, and `dashboard.html` with a pass-rate gauge, and publishes the pass rate to the GitHub Job Summary.
7. The default quality gate requires a pass rate >= 95% and zero failed tests tagged `critical`.

## Repository Structure

```text
.github/workflows/       GitHub Actions workflows
config/environments/     Robot Framework environment variables
features/approved/       Manually approved Gherkin scenarios
features/pending/        AI-generated scenarios pending approval
resources/               Reusable Robot Framework resources and keywords
scripts/                 Jira, AI, metrics, dashboard and quality-gate utilities
tests/api/               API tests using RequestsLibrary
tests/ui/                UI tests using Browser Library
```

## GitHub Secrets

- `JIRA_BASE_URL`
- `JIRA_EMAIL`
- `JIRA_API_TOKEN`
- `AI_API_KEY`
- `TEST_USER`
- `TEST_PASSWORD`
- `SONAR_TOKEN`, optional
- `SONAR_HOST_URL`, optional

## GitHub Variables

- `AI_BASE_URL`
- `AI_MODEL`
- `MIN_PASS_RATE`
- `MAX_CRITICAL_FAILURES`
- `INTEGRATION_WEB_BASE_URL`
- `INTEGRATION_API_BASE_URL`
- `TEST_WEB_BASE_URL`
- `TEST_API_BASE_URL`

## GitHub Environments

Create these environments:

- `integration`
- `test`
- `gherkin-approval`

Configure **Required Reviewers** on `gherkin-approval` to enforce human validation before generated test specifications are accepted.

## AI Provider

The included AI client uses an OpenAI Chat Completions-compatible API contract. It can be configured for GitHub Models, Azure OpenAI through a compatible gateway, OpenAI, or another compatible provider by setting `AI_BASE_URL`, `AI_MODEL`, and `AI_API_KEY`.

The Gherkin-generation prompt enforces:

- Maximum of five step lines per Scenario or Scenario Outline
- `Examples` data tables when data variation is useful
- Jira issue key tags for traceability
- `@needs-clarification` when requirements are ambiguous
- No invented business rules

## Local Execution

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
rfbrowser init
robot --variablefile config/environments/integration.py --outputdir results tests
python scripts/metrics.py results/output.xml results/metrics.json
python scripts/dashboard.py results/metrics.json results/dashboard.html
python scripts/quality_gate.py results/metrics.json
```

## Quality Reporting

Robot Framework produces its native `report.html`, `log.html`, and `output.xml`. The project additionally creates:

- `metrics.json` with passed, failed, skipped, total, pass rate, and critical failures
- `dashboard.html` with a gauge-style pass-rate visualization
- GitHub Job Summary with execution statistics
- Pipeline failure when the configured quality thresholds are not met

## Before First Use

Replace example application URLs, configure GitHub Environments and secrets, update `CODEOWNERS`, and adapt Robot Framework resources to your actual API endpoints, selectors, authentication model, and business keywords. Never commit production credentials or tokens.
