# Graph Report - minprojai  (2026-11-20)

## Corpus Check
- 165 files · ~224,442 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 67 file(s) not represented in the graph (top: .csv 60, .tabpfn_fit 2, .ckpt 1)
- WARNING: 67 of 232 files seen (29%) have no supported extractor and are missing from this graph entirely. It may look complete while representing only part of the codebase.

## Summary
- 1345 nodes · 2361 edges · 70 communities (40 shown, 30 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 119 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- UI/UX Accessibility & QA
- Shadcn UI Installer
- Search & Tokenizer Engine
- UI/UX Accessibility & QA
- Design System Generator
- UI/UX Accessibility & QA
- Design System Generator
- Design System Generator
- Search & Tokenizer Engine
- Design System Generator
- Search & Tokenizer Engine
- Titanic Predictor & ML
- Shadcn UI Installer
- Design System Generator
- Search & Tokenizer Engine
- Search & Tokenizer Engine
- Design System Generator
- Testing & Validation 17
- Testing & Validation 18
- Design System Generator
- Titanic Predictor & ML
- Design System Generator
- Color Palette & Theming
- SVG & Icon Generation
- Brand & Corporate Identity
- Color Palette & Theming
- UI/UX Accessibility & QA
- Titanic Predictor & ML
- Testing & Validation 29
- UI/UX Accessibility & QA
- UI/UX Accessibility & QA
- Titanic Predictor & ML
- Brand & Corporate Identity
- Design System Generator
- Design System Generator
- Testing & Validation 36
- Titanic Predictor & ML
- Color Palette & Theming
- Design System Generator
- Testing & Validation 40
- Color Palette & Theming
- Titanic Predictor & ML
- Titanic Predictor & ML
- Color Palette & Theming
- Design System Generator
- Search & Tokenizer Engine
- Design System Generator
- UI/UX Accessibility & QA
- UI/UX Accessibility & QA
- Testing & Validation 55
- Design System Generator
- UI/UX Accessibility & QA
- Design System Generator
- UI/UX Accessibility & QA
- Brand & Corporate Identity
- Design System Generator
- Design System Generator
- Design System Generator
- Testing & Validation 65

## God Nodes (most connected - your core abstractions)
1. `TailwindConfigGenerator` - 58 edges
2. `TestTailwindConfigGenerator` - 35 edges
3. `DesignSystemGenerator` - 35 edges
4. `ShadcnInstaller` - 34 edges
5. `TestShadcnInstaller` - 26 edges
6. `TitanicUnitAndIntegrationTests` - 21 edges
7. `run_pipeline()` - 17 edges
8. `read_rows()` - 16 edges
9. `color` - 15 edges
10. `search()` - 15 edges

## Surprising Connections (you probably didn't know these)
- `TestGeneratedConfigIsValidJs` --uses--> `TailwindConfigGenerator`  [INFERRED]
  .agents/skills/ui-styling/scripts/tests/test_tailwind_config_gen.py → .agents/skills/ui-styling/scripts/tailwind_config_gen.py
- `TestTailwindConfigGenerator` --uses--> `TailwindConfigGenerator`  [INFERRED]
  .agents/skills/ui-styling/scripts/tests/test_tailwind_config_gen.py → .agents/skills/ui-styling/scripts/tailwind_config_gen.py
- `TestEndToEndCoherence` --uses--> `DesignSystemGenerator`  [INFERRED]
  .agents/skills/ui-ux-pro-max/scripts/tests/test_design_system_mode.py → .agents/skills/ui-ux-pro-max/scripts/design_system.py
- `TitanicUnitAndIntegrationTests` --uses--> `PredictorForm`  [INFERRED]
  website/predictor/tests.py → website/predictor/forms.py
- `predict_view()` --uses--> `MLService`  [INFERRED]
  website/predictor/views.py → website/predictor/ml_service.py

## Import Cycles
- None detected.

## Communities (70 total, 30 thin omitted)

### Community 0 - "UI/UX Accessibility & QA"
Cohesion: 0.06
Nodes (44): read_rows(), TestAccessibilityGuidance, TestChartsTypographyAndIcons, TestCurrentReactGuidance, TestSemanticColors, TestGeneratedCatalogContract, _catalog_date(), _check_app_interface_contract() (+36 more)

### Community 1 - "Shadcn UI Installer"
Cohesion: 0.05
Nodes (3): main(), ShadcnInstaller, TestShadcnInstaller

### Community 2 - "Search & Tokenizer Engine"
Cohesion: 0.06
Nodes (31): BM25, _contains_phrase(), detect_domain(), _domain_keywords(), _exact_match_diagnostic(), _exact_row_identity(), _exact_stack_identifier(), _file_signature() (+23 more)

### Community 3 - "UI/UX Accessibility & QA"
Cohesion: 0.06
Nodes (13): DesignSystemGenerator, _resolve_dial(), apply_decision_rules(), _object_without_duplicates(), parse_decision_rules(), _validate_action(), TestReasoningMatch, read_rows() (+5 more)

### Community 4 - "Design System Generator"
Cohesion: 0.06
Nodes (25): apply_color(), apply_viewbox_size(), extract_svgs(), generate_batch(), generate_icon(), generate_sizes(), load_env(), main() (+17 more)

### Community 5 - "UI/UX Accessibility & QA"
Cohesion: 0.05
Nodes (15): _contrast_ratio(), _derive_dark_palette(), _filter_anti_patterns_for_mode(), _palette_is_dark(), _query_wants_dark(), _relative_luminance(), _resolve_color_mode(), _select_palette_for_mode() (+7 more)

### Community 6 - "Design System Generator"
Cohesion: 0.05
Nodes (53): $type, $value, $type, $value, $type, $value, $type, $value (+45 more)

### Community 7 - "Design System Generator"
Cohesion: 0.04
Nodes (48): $type, $value, background, destructive, destructive-foreground, foreground, muted, muted-foreground (+40 more)

### Community 8 - "Search & Tokenizer Engine"
Cohesion: 0.06
Nodes (13): BM25, detect_domain(), get_cip_brief(), _load_csv(), search(), search_all(), _search_csv(), BM25 (+5 more)

### Community 9 - "Design System Generator"
Cohesion: 0.06
Nodes (45): $type, $value, $type, $value, bg, fg, font-size, hover-bg (+37 more)

### Community 10 - "Search & Tokenizer Engine"
Cohesion: 0.08
Nodes (17): format_context(), format_result(), main(), BM25, calculate_pattern_break(), detect_domain(), get_background_config(), get_color_for_emotion() (+9 more)

### Community 11 - "Titanic Predictor & ML"
Cohesion: 0.09
Nodes (10): compute_all_metrics(), plot_calibration_curve(), plot_confusion_matrix(), plot_pr_curve(), plot_probability_histogram(), plot_roc_curve(), df_to_markdown_table(), generate_markdown_report() (+2 more)

### Community 12 - "Shadcn UI Installer"
Cohesion: 0.11
Nodes (5): test_sync_parses_bundled_starter_template(), main(), _run(), test_flags_hardcoded_hex_sharing_line_with_token(), test_token_only_line_reports_no_violation()

### Community 13 - "Design System Generator"
Cohesion: 0.06
Nodes (34): $type, $value, $type, $value, $type, $value, $type, $value (+26 more)

### Community 14 - "Search & Tokenizer Engine"
Cohesion: 0.08
Nodes (12): ansi_ljust(), _detect_page_type(), format_ascii_box(), format_master_md(), format_page_override_md(), _generate_intelligent_overrides(), hex_to_ansi(), persist_design_system() (+4 more)

### Community 15 - "Search & Tokenizer Engine"
Cohesion: 0.12
Nodes (9): build_cip_prompt(), check_logo_required(), generate_cip_set(), generate_with_nano_banana(), load_env(), load_logo_image(), main(), format_output() (+1 more)

### Community 16 - "Design System Generator"
Cohesion: 0.13
Nodes (11): _e(), generate_chart_slide(), generate_cta_slide(), generate_deck(), generate_metrics_slide(), generate_problem_slide(), generate_solution_slide(), generate_testimonial_slide() (+3 more)

### Community 19 - "Design System Generator"
Cohesion: 0.16
Nodes (9): generate_css_for_background(), get_background_image(), get_curated_images(), get_overlay_css(), get_pexels_search_url(), load_backgrounds_config(), load_brand_colors(), main() (+1 more)

### Community 21 - "Design System Generator"
Cohesion: 0.12
Nodes (16): $type, $value, $type, $value, $type, $value, $type, $value (+8 more)

### Community 23 - "Color Palette & Theming"
Cohesion: 0.20
Nodes (11): calculateCompliance(), colorDistance(), displayPalette(), extractHexColors(), findNearestBrandColor(), fs, generateImageMagickCommand(), hexToRgb() (+3 more)

### Community 25 - "Brand & Corporate Identity"
Cohesion: 0.25
Nodes (13): checkManifest(), formatBytes(), formatOutput(), fs, main(), parseFilename(), path, RULES (+5 more)

### Community 28 - "Titanic Predictor & ML"
Cohesion: 0.19
Nodes (4): _build_match_result(), get_historical_df(), match_passenger(), normalize_text()

### Community 33 - "Brand & Corporate Identity"
Cohesion: 0.23
Nodes (4): generate_html(), get_deliverable_info(), get_image_base64(), main()

### Community 34 - "Design System Generator"
Cohesion: 0.17
Nodes (8): args, fs, minimal, MINIMAL_TOKENS, path, projectRoot, tokensPath, wrapStyle

### Community 35 - "Design System Generator"
Cohesion: 0.24
Nodes (11): extensions, formatReport(), fs, getFiles(), main(), parseArgs(), path, patterns (+3 more)

### Community 36 - "Testing & Validation 36"
Cohesion: 0.18
Nodes (3): read_rows(), TestTextLayoutDataContracts, TestTextLayoutRetrieval

### Community 37 - "Titanic Predictor & ML"
Cohesion: 0.21
Nodes (3): load_categories(), format_match_message(), get_crew_sentence()

### Community 38 - "Color Palette & Theming"
Cohesion: 0.31
Nodes (10): extractColorsFromTable(), extractCoreAttributes(), extractHexColors(), extractImageStyle(), extractTypography(), extractVoice(), fs, generatePromptAddition() (+2 more)

### Community 39 - "Design System Generator"
Cohesion: 0.18
Nodes (11): fast, normal, slow, $type, $value, $type, $value, primitive (+3 more)

### Community 42 - "Titanic Predictor & ML"
Cohesion: 0.24
Nodes (4): get_musician_sentence(), get_current_lang(), how_it_works_view(), predict_view()

### Community 44 - "Color Palette & Theming"
Cohesion: 0.29
Nodes (8): adjustBrightness(), { execFileSync }, extractColorsFromMarkdown(), fs, generateColorScale(), main(), path, updateDesignTokens()

### Community 45 - "Design System Generator"
Cohesion: 0.36
Nodes (9): flattenTokens(), fs, generateCSS(), generateTailwind(), main(), parseArgs(), path, resolveReference() (+1 more)

### Community 47 - "Search & Tokenizer Engine"
Cohesion: 0.32
Nodes (3): format_brief(), format_results(), main()

### Community 48 - "Design System Generator"
Cohesion: 0.29
Nodes (8): $type, $value, $type, $value, radius, default, full, default

### Community 52 - "UI/UX Accessibility & QA"
Cohesion: 0.29
Nodes (3): format_markdown(), generate_design_system(), TestPersistence

### Community 57 - "Design System Generator"
Cohesion: 0.47
Nodes (6): sm, shadow, sm, sm, $type, $value

### Community 59 - "Design System Generator"
Cohesion: 0.60
Nodes (5): lg, $type, $value, lg, lg

### Community 62 - "Design System Generator"
Cohesion: 0.67
Nodes (4): xl, xl, $type, $value

### Community 63 - "Design System Generator"
Cohesion: 0.67
Nodes (4): $type, $value, md, md

### Community 64 - "Design System Generator"
Cohesion: 0.67
Nodes (4): $type, $value, none, none

## Knowledge Gaps
- **30 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `TailwindConfigGenerator` connect `Color Palette & Theming` to `Testing & Validation 40`, `Shadcn UI Installer`, `Any`, `Testing & Validation 49`, `Testing & Validation 50`, `Color Palette & Theming`, `Testing & Validation 17`, `Testing & Validation 54`, `Testing & Validation 22`, `Testing & Validation 29`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `TailwindConfigGenerator` (e.g. with `TestGeneratedConfigIsValidJs` and `TestTailwindConfigGenerator`) actually correct?**
  _`TailwindConfigGenerator` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Should `UI/UX Accessibility & QA` be split into smaller, more focused modules?**
  _Cohesion score 0.06025039123630673 - nodes in this community are weakly interconnected._
- **Why does `ShadcnInstaller` connect `Shadcn UI Installer` to `Shadcn UI Installer`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `DesignSystemGenerator` (e.g. with `TestReasoningMatch` and `TestReasoningContract`) actually correct?**
  _`DesignSystemGenerator` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `Shadcn UI Installer` be split into smaller, more focused modules?**
  _Cohesion score 0.053555750658472345 - nodes in this community are weakly interconnected._
- **Why does `main()` connect `Testing & Validation 40` to `Shadcn UI Installer`, `Search & Tokenizer Engine`, `Testing & Validation 49`, `Testing & Validation 50`, `Color Palette & Theming`, `Testing & Validation 54`, `Testing & Validation 22`, `Color Palette & Theming`, `Testing & Validation 29`?**
  _High betweenness centrality (0.032) - this node is a cross-community bridge._