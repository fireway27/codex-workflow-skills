# General Development Skills — 한국어판

일반적인 소프트웨어 개발 업무에 사용하는 Codex Skill 5종입니다. 특정 대회나 평가를 전제로 하지 않습니다.

| Skill | 용도 |
|---|---|
| `requirements-analysis` | 요구사항과 완료 기준 분석 |
| `task-planning` | 작업 분해·우선순위·의존성 정리 |
| `testing-debugging` | 오류 재현·수정·재검증 |
| `code-quality-review` | 정확성·보안·유지보수성 검토 |
| `decision-documentation` | 선택 근거·대안·검증 기록 |

## 사용

프로젝트 루트에 `.agents/skills/` 폴더를 배치하고 Codex에서 `/skills`로 인식 여부를 확인합니다. Codex 버전과 실행 환경에 따라 재시작이나 별도 설치 절차가 필요할 수 있습니다.

예시: `$requirements-analysis README를 분석하고 완료 기준을 정리해 주세요.`

## 운영 원칙

- 파일명, Skill 호출명, YAML 메타데이터 키는 영문으로 유지하고 설명·본문은 한국어로 작성했습니다.
- 실제 수행한 작업·테스트만 보고하며, 근거 없는 성공 주장과 작업 기록 조작을 금지합니다.
- 외부 전송·도구 설치는 사용 환경의 정책을 확인해야 합니다.
- 공개 저장소에 게시하거나 특정 환경에 반입하기 전에 해당 환경의 허용 규정을 확인하세요.
