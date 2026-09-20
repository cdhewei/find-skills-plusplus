# -*- coding: utf-8 -*-
"""回归：find-skills++ 必须能给自己打分（自检）。

背景（真实缺陷）：discover_local 无条件排除自身目录名，导致
`quality find-skills-plusplus` 报「未找到该技能」——一个宣称能做质量评级的
工具评不了自己，出场演示当场穿帮。

修复：discover_local 增加 include_self 参数；quality 自检时包含自身，
并支持 `self` / `find-skills++` 等别名。默认仍排除自己（避免搜索结果自荐）。
"""
import io
import contextlib

import findskills


def test_discover_local_excludes_self_by_default():
    """默认不列出自己——搜索结果里不该自荐。"""
    names = {s["slug"] for s in findskills.discover_local()}
    assert findskills.SELF_SLUG not in names


def test_discover_local_include_self():
    """include_self=True 时能找到自己。"""
    names = {s["slug"] for s in findskills.discover_local(include_self=True)}
    assert findskills.SELF_SLUG in names


def test_quality_self_alias_runs():
    """`quality self` 必须能跑通并给出评分，不报「未找到」。"""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = findskills.main(["quality", "self"])
    out = buf.getvalue()
    assert rc == 0, f"quality self 失败，输出：{out}"
    assert "未找到" not in out
    assert "分" in out or "评级" in out or "质量" in out


def test_quality_by_slug_runs():
    """用完整 slug 也应能定位到自己。"""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = findskills.main(["quality", "find-skills-plusplus"])
    out = buf.getvalue()
    assert rc == 0, f"quality <slug> 失败，输出：{out}"
    assert "未找到" not in out
