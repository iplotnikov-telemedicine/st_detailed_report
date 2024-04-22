with custom_profile as (
	SELECT
		epfv.organisation_id,
		epfv.employee_id,
		pft.json_view_type,
		pf.profile_field_id,
		pf.parent_field_id,
	   	pf.name as field_name,
	   	ps.name as section_name,
	   	epfv.field_value,
	   	count(pf.profile_field_id) over (partition by epfv.organisation_id, epfv.employee_id, pf.name) as same_field_name_count
	   FROM profile_field pf
	   INNER JOIN profile_field_type pft
		ON pf.profile_field_type_id = pft.profile_field_type_id
	   INNER JOIN employee_profile_field_value epfv
	    ON pf.profile_field_id = epfv.profile_field_id
	   LEFT JOIN profile_section ps
		    ON pf.profile_section_id = ps.profile_section_id
	   WHERE 1=1
	   	AND pf.hidden is false
	   	AND pf.parent_field_id is null
	   	AND pft.json_view_type not in ('OBJECT_VIEW_TYPE', 'LIST_VIEW_TYPE')
)
    SELECT
    	organisation_id,
		employee_id,
		section_name,
		field_name || ' (' || section_name || ')' as field_name, 
    	field_value
    FROM custom_profile