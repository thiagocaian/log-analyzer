import argparse
from src import log_analyzer as la

def build_parser():
    p = argparse.ArgumentParser(description="Analisador simples de logs (auth, access).")
    sub = p.add_subparsers(dest="cmd", required=True)

    pa = sub.add_parser("auth", help="Analisar auth.log (falhas de senha)")
    pa.add_argument("--file", required=True, help="Caminho do auth.log")
    pa.add_argument("--json", help="Salvar agregação por IP em JSON")
    pa.add_argument("--csv", help="Salvar agregação por IP em CSV")

    px = sub.add_parser("access", help="Analisar access.log (Nginx)")
    px.add_argument("--file", required=True, help="Caminho do access.log")
    px.add_argument("--json", help="Salvar agregação por IP em JSON")
    px.add_argument("--csv", help="Salvar agregação por IP em CSV")
    return p

def main():
    args = build_parser().parse_args()

    if args.cmd == "auth":
        agg = la.aggregate_auth_by_ip(args.file)
        print(f"[auth] IPs únicos: {len(agg)} — tentativas totais: {sum(agg.values())}")
        top = sorted(agg.items(), key=lambda x: (-x[1], x[0]))[:5]
        for ip, cnt in top:
            print(f"  {ip:<15} {cnt:>5}")
        if args.json:
            la.export_json(agg, args.json); print(f"JSON salvo em {args.json}")
        if args.csv:
            la.export_csv(agg, args.csv);   print(f"CSV salvo em {args.csv}")

    elif args.cmd == "access":
        agg = la.aggregate_access_by_ip(args.file)
        print(f"[access] IPs únicos: {len(agg)} — requisições totais: {sum(agg.values())}")
        top = sorted(agg.items(), key=lambda x: (-x[1], x[0]))[:5]
        for ip, cnt in top:
            print(f"  {ip:<15} {cnt:>5}")
        if args.json:
            la.export_json(agg, args.json); print(f"JSON salvo em {args.json}")
        if args.csv:
            la.export_csv(agg, args.csv);   print(f"CSV salvo em {args.csv}")

if __name__ == "__main__":
    main()
