-- ============================================================================
-- ODPS-Compatible Version (No odps.sql.decimal.odps2 required)
-- ============================================================================
-- This version uses DOUBLE instead of DECIMAL(precision,scale) to avoid
-- requiring the odps2 setting. Values are still rounded to 1 decimal place.
-- ============================================================================

-- Step 4: Final Consumer × Influencer Scores Table (TOP 20 INFLUENCERS)
CREATE TABLE IF NOT EXISTS lha_research_dev.consumer_influencer_loyalty_scores AS
SELECT
    m.visitor_id,
    m.influencer_id,

    -- Raw metrics from Step 1 (6 months) - optimized storage
    m.purchases_6m,  -- COUNT, already integer
    CAST(ROUND(m.spend_6m, 1) AS DOUBLE) AS spend_6m,
    m.unique_feeds_6m,  -- COUNT DISTINCT, already integer
    CAST(ROUND(m.total_stay_hours_6m, 1) AS DOUBLE) AS total_stay_hours_6m,

    -- Raw metrics from Step 1 (2 months) - optimized storage
    m.purchases_2m,  -- COUNT, already integer
    CAST(ROUND(m.spend_2m, 1) AS DOUBLE) AS spend_2m,
    m.unique_feeds_2m,  -- COUNT DISTINCT, already integer
    CAST(ROUND(m.total_stay_hours_2m, 1) AS DOUBLE) AS total_stay_hours_2m,

    -- Per-consumer max values from Step 3 (for normalization later) - optimized storage
    mx.max_purchases_6m,  -- MAX of COUNT, already integer
    CAST(ROUND(mx.max_spend_6m, 1) AS DOUBLE) AS max_spend_6m,
    mx.max_unique_feeds_6m,  -- MAX of COUNT DISTINCT, already integer
    CAST(ROUND(mx.max_total_hours_6m, 1) AS DOUBLE) AS max_total_hours_6m,
    mx.max_purchases_2m,  -- MAX of COUNT, already integer
    CAST(ROUND(mx.max_spend_2m, 1) AS DOUBLE) AS max_spend_2m,
    mx.max_unique_feeds_2m,  -- MAX of COUNT DISTINCT, already integer
    CAST(ROUND(mx.max_total_hours_2m, 1) AS DOUBLE) AS max_total_hours_2m,

    -- Consumer totals from Step 2 (for exclusivity calculation later) - optimized storage
    t.total_purchases_6m,  -- COUNT DISTINCT, already integer
    CAST(ROUND(t.total_spend_6m, 1) AS DOUBLE) AS total_spend_6m,
    t.total_unique_feeds_6m,  -- COUNT DISTINCT, already integer
    CAST(ROUND(t.total_stay_hours_6m, 1) AS DOUBLE) AS total_stay_hours_6m,
    t.total_purchases_2m,  -- COUNT DISTINCT, already integer
    CAST(ROUND(t.total_spend_2m, 1) AS DOUBLE) AS total_spend_2m,
    t.total_unique_feeds_2m,  -- COUNT DISTINCT, already integer
    CAST(ROUND(t.total_stay_hours_2m, 1) AS DOUBLE) AS total_stay_hours_2m

FROM tmp_consumer_influencer_metricsb m
LEFT JOIN tmp_consumer_influencer_totals t
    ON m.visitor_id = t.visitor_id
LEFT JOIN lha_research_dev.tmp_consumer_influencer_max mx
    ON m.visitor_id = mx.visitor_id
;
