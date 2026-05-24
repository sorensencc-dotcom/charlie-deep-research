.PHONY: a b both clean help

help:
	@echo "CIC Master Sheet Builder"
	@echo ""
	@echo "Targets:"
	@echo "  make a       - Generate variant A (Raster-Embedded)"
	@echo "  make b       - Generate variant B (Full-SVG)"
	@echo "  make both    - Generate both variants"
	@echo "  make clean   - Remove all generated master sheets"
	@echo "  make diagrams - Regenerate diagram templates"

a:
	python generate_master_sheet.py A
	@echo "✓ Variant A generated"

b:
	python generate_master_sheet.py B
	@echo "✓ Variant B generated"

both: a b
	@echo "✓ Both variants complete"

diagrams:
	python generate_diagrams.py
	@echo "✓ Diagrams regenerated"

clean:
	rm -f master_sheet_*.svg
	@echo "✓ Cleaned"
