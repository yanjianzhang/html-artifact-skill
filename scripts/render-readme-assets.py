#!/usr/bin/env python3
"""Generate lightweight README preview assets for the HTML artifact skill.

The skill intentionally keeps these assets dependency-free so contributors can
refresh the README gallery without installing a browser stack. The generated
SVGs are representative previews of the checked-in demo HTML files.
"""

from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "readme"


def svg(width: int, height: int, body: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="HTML artifact preview">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#eef4ff"/>
      <stop offset="55%" stop-color="#f8fafc"/>
      <stop offset="100%" stop-color="#ecfdf3"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="150%">
      <feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#101828" flood-opacity=".16"/>
    </filter>
  </defs>
  <rect width="100%" height="100%" fill="url(#bg)"/>
  {body}
</svg>
"""


def text(x: int, y: int, value: str, *, size: int = 22, weight: int = 650, color: str = "#172033") -> str:
    return (
        f'<text x="{x}" y="{y}" fill="{color}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" '
        f'font-size="{size}" font-weight="{weight}">{escape(value)}</text>'
    )


def pill(x: int, y: int, value: str, fill: str, color: str, width: int | None = None) -> str:
    width = width or max(92, len(value) * 9 + 28)
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="34" rx="17" fill="{fill}" stroke="#d9e0ea"/>'
        + text(x + 16, y + 23, value, size=14, weight=800, color=color)
    )


def card(x: int, y: int, w: int, h: int, title: str, lines: list[str], accent: str = "#2457c5") -> str:
    body = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="#fff" stroke="#d9e0ea"/>']
    body.append(f'<rect x="{x}" y="{y}" width="6" height="{h}" rx="3" fill="{accent}"/>')
    body.append(text(x + 22, y + 36, title, size=19, weight=800))
    for idx, line in enumerate(lines):
        body.append(text(x + 22, y + 68 + idx * 26, line, size=15, weight=520, color="#475467"))
    return "\n".join(body)


def decision_report() -> str:
    cards = "\n".join(
        [
            card(72, 234, 296, 184, "Recommendation", ["Ship staged rollout", "after one more gate"], "#15803d"),
            card(392, 234, 296, 184, "Main Risk", ["Segment variance is", "hidden by headline F1"], "#b45309"),
            card(712, 234, 296, 184, "Next Action", ["Export gate checklist", "for the next agent"], "#2457c5"),
        ]
    )
    table = [
        '<rect x="72" y="456" width="936" height="184" rx="18" fill="#fff" stroke="#d9e0ea"/>',
        text(100, 496, "Evidence Matrix", size=20, weight=800),
        '<line x1="100" y1="518" x2="980" y2="518" stroke="#d9e0ea"/>',
        text(100, 552, "Option", size=14, weight=800, color="#667085"),
        text(300, 552, "Evidence", size=14, weight=800, color="#667085"),
        text(612, 552, "Risk", size=14, weight=800, color="#667085"),
        text(820, 552, "Decision", size=14, weight=800, color="#667085"),
        text(100, 592, "Staged rollout", size=16),
        text(300, 592, "Best quality/cost ratio", size=16, color="#475467"),
        text(612, 592, "Needs segment gate", size=16, color="#475467"),
        pill(820, 568, "recommended", "#ecfdf3", "#15803d", 138),
    ]
    body = "\n".join(
        [
            '<rect x="48" y="42" width="984" height="640" rx="28" fill="#ffffff" opacity=".88" filter="url(#shadow)"/>',
            text(78, 102, "Decision Report Demo", size=38, weight=850),
            text(80, 142, "Cards, evidence, language switch, and export controls in one browser artifact.", size=19, weight=520, color="#667085"),
            pill(78, 166, "bilingual", "#eef4ff", "#2457c5"),
            pill(190, 166, "decision-ready", "#ecfdf3", "#15803d", 150),
            pill(360, 166, "exportable", "#fff7ed", "#b45309"),
            cards,
            "\n".join(table),
        ]
    )
    return svg(1080, 720, body)


def interactive_review() -> str:
    rows = []
    severities = [
        ("Blocker", "Session expiry not enforced", "src/auth/session.ts", "#fef3f2", "#b42318"),
        ("Major", "Webhook can double-apply", "src/billing/webhook.ts", "#fff7ed", "#b45309"),
        ("Major", "Cache stale after import", "src/dashboard/cache.ts", "#fff7ed", "#b45309"),
    ]
    for i, (sev, finding, file_name, fill, color) in enumerate(severities):
        y = 362 + i * 72
        rows.extend(
            [
                f'<rect x="78" y="{y}" width="924" height="60" rx="12" fill="#fff" stroke="#d9e0ea"/>',
                pill(102, y + 13, sev, fill, color, 96),
                text(230, y + 37, finding, size=17, weight=700),
                text(610, y + 37, file_name, size=15, weight=560, color="#667085"),
            ]
        )
    body = "\n".join(
        [
            '<rect x="48" y="42" width="984" height="640" rx="28" fill="#ffffff" opacity=".88" filter="url(#shadow)"/>',
            text(78, 102, "Interactive Review Demo", size=38, weight=850),
            text(80, 142, "Search, filter, and export only the findings that matter.", size=19, weight=520, color="#667085"),
            '<rect x="78" y="192" width="360" height="46" rx="14" fill="#fff" stroke="#cbd5e1"/>',
            text(104, 222, "Search: billing", size=17, weight=650, color="#475467"),
            '<rect x="458" y="192" width="180" height="46" rx="14" fill="#fff" stroke="#cbd5e1"/>',
            text(484, 222, "Severity: Major", size=17, weight=650, color="#475467"),
            '<rect x="658" y="192" width="180" height="46" rx="14" fill="#ecfdf3" stroke="#86efac"/>',
            text(684, 222, "Copy visible", size=17, weight=760, color="#15803d"),
            text(78, 292, "Filtered Findings", size=23, weight=830),
            "\n".join(rows),
            '<rect x="78" y="600" width="924" height="40" rx="12" fill="#101828"/>',
            text(104, 626, '[{ "severity": "Major", "file": "src/billing/webhook.ts" }]', size=15, weight=560, color="#f9fafb"),
        ]
    )
    return svg(1080, 720, body)


def formula_report() -> str:
    formula_one = [
        ("TP", "|{ g in G : exists l in L, match(g,l) and specific(l,g) }|"),
        ("Precision", "TP / (TP + FP)"),
        ("Recall", "TP / |G|"),
        ("F1", "2 x Precision x Recall / (Precision + Recall)"),
    ]
    formula_two = [
        ("DeltaCovered", "|Covered(L_after) \\ Covered(L_before)|"),
        ("AddedLeaves", "|L_after \\ L_before|"),
        ("Yield", "(DeltaCovered / AddedLeaves) x SpecificityMean"),
    ]

    def formula_card(x: int, y: int, title: str, rows: list[tuple[str, str]]) -> str:
        out = [
            f'<rect x="{x}" y="{y}" width="430" height="330" rx="20" fill="#fff" stroke="#d9e0ea"/>',
            text(x + 24, y + 42, title, size=22, weight=830),
            f'<rect x="{x + 24}" y="{y + 70}" width="382" height="210" rx="16" fill="#f8fafc" stroke="#d9e0ea"/>',
        ]
        for idx, (lhs, rhs) in enumerate(rows):
            yy = y + 112 + idx * 42
            out.append(text(x + 46, yy, lhs, size=18, weight=700, color="#172033"))
            out.append(text(x + 178, yy, "=", size=18, weight=700, color="#667085"))
            out.append(text(x + 206, yy, rhs, size=15, weight=520, color="#344054"))
        out.append(text(x + 24, y + 308, "Mobile-safe horizontal scroll fallback", size=14, weight=650, color="#667085"))
        return "\n".join(out)

    body = "\n".join(
        [
            '<rect x="48" y="42" width="984" height="640" rx="28" fill="#ffffff" opacity=".88" filter="url(#shadow)"/>',
            text(78, 102, "Formula-Heavy Report Demo", size=38, weight=850),
            text(80, 142, "Equations are readable math blocks, not dark code snippets.", size=19, weight=520, color="#667085"),
            pill(78, 166, "aligned math", "#eef4ff", "#2457c5", 132),
            pill(230, 166, "scroll fallback", "#ecfdf3", "#15803d", 150),
            formula_card(78, 244, "Specificity-safe F1", formula_one),
            formula_card(562, 244, "Expansion Yield", formula_two),
        ]
    )
    return svg(1080, 720, body)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    assets = {
        "decision-report.svg": decision_report(),
        "filter-interaction.svg": interactive_review(),
        "formula-report.svg": formula_report(),
    }
    for filename, content in assets.items():
        (OUT_DIR / filename).write_text(content, encoding="utf-8")
        print(f"wrote {OUT_DIR / filename}")


if __name__ == "__main__":
    main()
