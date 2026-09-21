import argparse,json
from pathlib import Path
from .analyst import analyse
from .llm import enrich
def main():
    p=argparse.ArgumentParser(description="Safe simulated incident assistant");p.add_argument("--incident",required=True);p.add_argument("--mode",choices=["local","openai"],default="local");p.add_argument("--output");a=p.parse_args()
    incident=json.loads(Path(a.incident).read_text()); result=analyse(incident); provider="local-deterministic"
    if a.mode=="openai": result,provider=enrich(incident,result)
    result["provider"]=provider; rendered=json.dumps(result,indent=2); print(rendered)
    if a.output: Path(a.output).write_text(rendered+"\n")
if __name__=="__main__":main()
