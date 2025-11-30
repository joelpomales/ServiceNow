(function runTransformScript(source, map, log, target) {

    // 1. Disable the automatic system field updates
    // This allows us to manually set sys_created_on and sys_updated_on.
    target.autoSysFields(false);

    // 2. (Optional) Disable Business Rules
    // This is often needed for historical imports to prevent BRs from
    // overriding your imported values or running unnecessary logic.
    // Use with caution, as you might need some BRs to run.
    // target.setWorkflow(false);

    // 3. Map the system date fields
    // You must map the target fields manually in the script.
    // Ensure the date format in the source is correct.
    if (source.u_create_date) {
        target.sys_created_on = source.u_create_date;
    }

    if (source.u_update_date) {
        target.sys_updated_on = source.u_update_date;
    }

})(source, map, log, target);