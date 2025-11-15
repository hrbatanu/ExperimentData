# Variable Documentation: Loyalty and Exclusivity Scores

## Table 1: consumer_influencer_loyalty_scores_b

### Identifiers
- **visitor_id**: Unique consumer identifier
- **influencer_id**: Unique influencer identifier (one of 20 sampled influencers)

### Consumer-Influencer Engagement Metrics (6-month window)
- **purchases_6m**: Number of purchases consumer made from this specific influencer in 6-month window
- **spend_6m**: Total monetary spending by consumer on this influencer's products in 6-month window
- **unique_feeds_6m**: Number of unique content feeds consumer viewed from this influencer in 6-month window
- **stay_hours_6m**: Total hours consumer spent viewing this influencer's content in 6-month window

### Consumer-Influencer Engagement Metrics (2-month window)
- **purchases_2m**: Number of purchases consumer made from this specific influencer in 2-month window
- **spend_2m**: Total monetary spending by consumer on this influencer's products in 2-month window
- **unique_feeds_2m**: Number of unique content feeds consumer viewed from this influencer in 2-month window
- **stay_hours_2m**: Total hours consumer spent viewing this influencer's content in 2-month window

### Normalization Bounds (for Loyalty Scores) - 6-month window
These represent the consumer's maximum engagement with ANY influencer (across ALL influencers on platform, not just the 20 sampled):
- **max_purchases_6m**: Consumer's highest purchase count from their most-purchased influencer
- **max_spend_6m**: Consumer's highest spending amount on their most-spent influencer
- **max_unique_feeds_6m**: Consumer's highest unique feed count from their most-viewed influencer
- **max_total_hours_6m**: Consumer's highest time spent on their most-engaged influencer

### Normalization Bounds (for Loyalty Scores) - 2-month window
- **max_purchases_2m**: Consumer's highest purchase count from their most-purchased influencer
- **max_spend_2m**: Consumer's highest spending amount on their most-spent influencer
- **max_unique_feeds_2m**: Consumer's highest unique feed count from their most-viewed influencer
- **max_total_hours_2m**: Consumer's highest time spent on their most-engaged influencer

### Total Activity (for Exclusivity Scores) - 6-month window
Consumer's total engagement across ALL influencers on platform:
- **total_purchases_6m**: Consumer's total purchase count from all influencers combined
- **total_spend_6m**: Consumer's total spending on all influencers combined
- **total_unique_feeds_6m**: Consumer's total unique feeds viewed across all influencers
- **total_stay_hours_6m**: Consumer's total hours spent on all influencers combined

### Total Activity (for Exclusivity Scores) - 2-month window
- **total_purchases_2m**: Consumer's total purchase count from all influencers combined
- **total_spend_2m**: Consumer's total spending on all influencers combined
- **total_unique_feeds_2m**: Consumer's total unique feeds viewed across all influencers
- **total_stay_hours_2m**: Consumer's total hours spent on all influencers combined

### Derived Metrics (Calculated from Above)

**Loyalty Scores (0-1 scale):**
- Loyalty_purchases_6m = purchases_6m / max_purchases_6m
- Loyalty_spend_6m = spend_6m / max_spend_6m
- Loyalty_feeds_6m = unique_feeds_6m / max_unique_feeds_6m
- Loyalty_hours_6m = stay_hours_6m / max_total_hours_6m
- *(Similar for 2m window)*

**Interpretation**: 1.0 = this is consumer's most-preferred influencer; 0.8 = consumer engages with this influencer at 80% the level of their top influencer

**Exclusivity Scores (0-1 scale):**
- Exclusivity_purchases_6m = purchases_6m / total_purchases_6m
- Exclusivity_spend_6m = spend_6m / total_spend_6m
- Exclusivity_feeds_6m = unique_feeds_6m / total_unique_feeds_6m
- Exclusivity_hours_6m = stay_hours_6m / total_stay_hours_6m
- *(Similar for 2m window)*

**Interpretation**: 0.3 = this influencer accounts for 30% of consumer's total influencer-related activity

---

## Table 2: consumer_brand_loyalty_scores_b

### Identifiers
- **visitor_id**: Unique consumer identifier
- **brand_id**: Unique brand identifier (one of 262 sampled brands)
- **major_category_id**: The product category where this brand generates the most revenue (brand's primary category assignment)

### Consumer-Brand Purchase Metrics (6-month window)
- **purchases_6m**: Number of purchases consumer made from this specific brand in 6-month window (across ALL categories, not filtered)
- **spend_6m**: Total monetary spending by consumer on this brand's products in 6-month window (across ALL categories)

### Consumer-Brand Purchase Metrics (2-month window)
- **purchases_2m**: Number of purchases consumer made from this specific brand in 2-month window
- **spend_2m**: Total monetary spending by consumer on this brand's products in 2-month window

### Normalization Bounds (for Loyalty Scores) - 6-month window
Consumer's maximum engagement with ANY brand (across ALL brands on platform, not just 262 sampled):
- **max_purchases_6m**: Consumer's highest purchase count from their most-purchased brand
- **max_spend_6m**: Consumer's highest spending amount on their most-spent brand

### Normalization Bounds (for Loyalty Scores) - 2-month window
- **max_purchases_2m**: Consumer's highest purchase count from their most-purchased brand
- **max_spend_2m**: Consumer's highest spending amount on their most-spent brand

### Category-Level Totals (for Within-Category Exclusivity) - 6-month window
Consumer's total activity within this brand's major category:
- **cat_total_purchases_6m**: Consumer's total purchases within this brand's major category (from all brands in category)
- **cat_total_spend_6m**: Consumer's total spending within this brand's major category (from all brands in category)

### Category-Level Totals (for Within-Category Exclusivity) - 2-month window
- **cat_total_purchases_2m**: Consumer's total purchases within this brand's major category
- **cat_total_spend_2m**: Consumer's total spending within this brand's major category

### Platform-Level Totals (for Cross-Brand Exclusivity) - 6-month window
Consumer's total activity across ALL brands:
- **total_purchases_6m**: Consumer's total purchase count from all brands combined
- **total_spend_6m**: Consumer's total spending on all brands combined

### Platform-Level Totals (for Cross-Brand Exclusivity) - 2-month window
- **total_purchases_2m**: Consumer's total purchase count from all brands combined
- **total_spend_2m**: Consumer's total spending on all brands combined

### Derived Metrics (Calculated from Above)

**Loyalty Scores (0-1 scale):**
- Loyalty_purchases_6m = purchases_6m / max_purchases_6m
- Loyalty_spend_6m = spend_6m / max_spend_6m
- *(Similar for 2m window)*

**Interpretation**: 1.0 = this is consumer's most-preferred brand; 0.8 = consumer purchases from this brand at 80% the level of their top brand

**Within-Category Exclusivity (0-1 scale):**
- Cat_exclusivity_purchases_6m = purchases_6m / cat_total_purchases_6m
- Cat_exclusivity_spend_6m = spend_6m / cat_total_spend_6m
- *(Similar for 2m window)*

**Interpretation**: 0.3 = this brand accounts for 30% of consumer's purchases within the category

**Cross-Brand Exclusivity (0-1 scale):**
- Total_exclusivity_purchases_6m = purchases_6m / total_purchases_6m
- Total_exclusivity_spend_6m = spend_6m / total_spend_6m
- *(Similar for 2m window)*

**Interpretation**: 0.3 = this brand accounts for 30% of consumer's total brand purchases across all categories

---

## Key Methodological Notes

1. **Data Structure**: Tables only contain records where consumers have actually purchased from the entity (no zero-padding for non-purchases)

2. **Normalization Scope**: Max values calculated from ALL entities on platform (not just sampled ones) to reflect true consumer preferences

3. **Exclusivity Denominators**: Always use ALL entities (not just sampled) to capture true exclusivity behavior

4. **Missing Values**: If a consumer-entity pair is absent from the table, it means the consumer has never purchased from that entity

5. **Time Windows**:
   - 6-month window captures long-term loyalty patterns
   - 2-month window captures recent engagement and potential shifts

6. **Brand Categories**: Each brand assigned to single "major category" based on revenue concentration, but purchase metrics include ALL categories
