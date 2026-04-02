def run_pipeline(pr):
    files = [f["filename"] for f in pr.get("files", [])]
    
    change_type = "refactor"
    if any(f["status"] == "added" for f in pr.get("files", [])):
        change_type = "feature"
    if any(f["status"] == "removed" for f in pr.get("files", [])):
        change_type = "removal"
    
    impact = "medium" if len(files) > 2 else "low"
    
    breaking_changes = any("TODO" in f.get("patch", "") for f in pr.get("files", []))
    
    comments = [c["body"] for c in pr.get("issue_comments", []) + pr.get("review_comments", [])]
    
    summary = f"PR '{pr['pull_request']['title']}' modifies {len(files)} files"

    return {
        "summary": summary,
        "files_changed": files,
        "change_type": change_type,
        "impact": impact,
        "breaking_changes": breaking_changes,
        "comments": comments
    }