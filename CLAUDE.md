# Croquet Rules

## CRITICAL: Live Websites - DO NOT MODIFY WITHOUT APPROVAL

Two croquet websites are LIVE community resources:

| Site | Local Path | Domain |
|------|------------|--------|
| **Abbotsford Croquet Club** | `croquet-abbotsford/` | abbotsfordcroquet.com |
| **Fraser Valley Croquet Society** | `FVCS/` | (check for live domain) |

**DO NOT** push, deploy, or modify these sites without explicit user approval.

Treat like production infrastructure - read-only unless specifically requested.

## Safe to Modify (with normal workflow)

These are experimental/personal projects:

| Folder | Purpose |
|--------|---------|
| `croquet-simulator/` | AI simulation project |
| `essick-croquet/` | Video annotation site (personal) |
| `ai-research/papers/croquet-ai/` | Research papers |
| `game-design/quiz-games/*croquet*` | Quiz games |
| `FVCS/croquet-GNN/` | ML experiments |
| `FVCS/croquet-rag/` | RAG experiments |

## Skills

| Skill | Purpose |
|-------|---------|
| `/croquet-opening-theory` | AC openings, drill app, practice cards |
| `/abbotsford-croquet` | Website management (requires approval to push) |
| `/croquet-notes` | Essick video annotations |
| `/video-analyze` | YouTube transcript analysis (default: croquet) |
| `/pnw-croquet-tournaments` | Tournament calendar tracking (PNW, CA, Canadian Nationals) |

## AC Drill App

- **Location**: `croquet-abbotsford/ac-drill.html`
- **Live URL**: https://abbotsfordcroquet.com/ac-drill.html
- **Features**: 14 opening combinations, progress tracking, PWA

## Development Workflow

For website changes:
1. Make changes locally
2. Test in browser
3. Show user the diff
4. Get explicit approval before `git push`

## Tournament Planning

- **Central folder**: `~/croquet-tournaments/`
- `pnw-2026.md` — Full tournament calendar, accommodation research, scan history
- `nationals-travel-2026.pdf` / `.tex` — Travel plan (flights, rental car, mallet transport)
- `nationals-budget-2026.md` — Budget tracker with estimates and actuals log

## Related To-Do Items

- Practice croquet drills (`/croquet-opening-theory`)
- Make a Croquet Drills app (new standalone app)
