# compare_engine.py
import json

def load_data():
    with open("lab_comparison_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def compare_labs(lab_a_key, lab_b_key):
    db = load_data()
    if lab_a_key not in db or lab_b_key not in db:
        print("Error: 지원하지 않는 연구실입니다. (현재 DIML, CVLab 지원)")
        return

    lab_a = db[lab_a_key]
    lab_b = db[lab_b_key]

    print("=" * 65)
    print(f"🔬 LABMATCH 1:1 비교 분석: [{lab_a['name']}] VS [{lab_b['name']}]")
    print("=" * 65)
    
    # 5대 핵심 체감 지표 출력
    metrics_keys = ["top_tier", "industry_collab", "career_path", "interdisciplinary", "lab_scale"]
    
    for idx, m_key in enumerate(metrics_keys, 1):
        m_a = lab_a["metrics"][m_key]
        m_b = lab_b["metrics"][m_key]
        print(f"\n[{idx}] {m_a['title']}")
        print(f"  👉 학부생 질문: \"{m_a['question']}\"")
        print(f"  • {lab_a_key}: {m_a['detail']}")
        print(f"  • {lab_b_key}: {m_b['detail']}")

    print("\n" + "=" * 65)
    print("📋 [학부생 맞춤 3줄 Visual Brief]")
    summary = db["comparison_summary"]
    print(f"• 공통점: {summary['common']}")
    print(f"• 차이점: {summary['difference']}")
    print("=" * 65)
    print("✉️ [면담/컨택용 추천 질문]")
    for q in summary["check_questions"]:
        print(f"• To {q['target']}: \"{q['question']}\"")
    print("=" * 65)

if __name__ == "__main__":
    compare_labs("DIML", "CVLab")
