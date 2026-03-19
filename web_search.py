#!/usr/bin/env python3
"""
Web search via DuckDuckGo.

Требования:
    pip install ddgs

Использование:
    python3 web_search.py "запрос"                         # базовый поиск
    python3 web_search.py "запрос" --max 20                # больше результатов
    python3 web_search.py "запрос" --domain github.com     # фильтр по домену
    python3 web_search.py "запрос" --period w              # за последнюю неделю
    python3 web_search.py "запрос" --period m              # за последний месяц
    python3 web_search.py "запрос" --period y              # за последний год
    python3 web_search.py "запрос" --json                  # вывод в JSON
    python3 web_search.py "запрос" --domain site.com --period w --max 5
"""

import argparse
import json
import sys

from ddgs import DDGS

PERIOD_MAP = {
    "d": "d",   # day
    "w": "w",   # week
    "m": "m",   # month
    "y": "y",   # year
}


def search(query: str, max_results: int = 10, domain: str = "", period: str = "",
           output_json: bool = False) -> None:
    # Apply domain filter by appending site: operator
    effective_query = query
    if domain:
        effective_query = f"site:{domain} {query}"

    # Map period to timelimit
    timelimit = PERIOD_MAP.get(period, None)

    with DDGS() as ddgs:
        kwargs = {"max_results": max_results}
        if timelimit:
            kwargs["timelimit"] = timelimit
        results = list(ddgs.text(effective_query, **kwargs))

    if not results:
        if output_json:
            print(json.dumps([], ensure_ascii=False))
        else:
            print("Ничего не найдено.")
        return

    if output_json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    for i, r in enumerate(results, 1):
        print(f"[{i}] {r.get('title', '—')}")
        print(f"    URL: {r.get('href', '—')}")
        print(f"    {r.get('body', '')}")
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web search via DuckDuckGo")
    parser.add_argument("query", nargs="+", help="Search query")
    parser.add_argument("--max", type=int, default=10, help="Max results (default: 10)")
    parser.add_argument("--domain", type=str, default="", help="Filter by domain (e.g. github.com)")
    parser.add_argument("--period", type=str, default="", choices=["d", "w", "m", "y", ""],
                        help="Time period: d=day, w=week, m=month, y=year")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()
    search(
        query=" ".join(args.query),
        max_results=args.max,
        domain=args.domain,
        period=args.period,
        output_json=args.json,
    )
