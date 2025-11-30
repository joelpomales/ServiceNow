# A comment
import csv
import random
from datetime import datetime, timedelta

# Services list provided
services = [
    "Taxware Enterprise Services",
    "Anaplan Enterprise Services",
    "Xactly Enterprise Services",
    "HireRight Enterprise Screening Management",
    "Xignite Enterprise Services",
    "DocuSign Enterprise Services",
    "SAP Enterprise Services",
    "SAP Financial Accounting",
    "SAP Materials Management",
    "SAP Controlling",
    "SAP Sales and Distribution",
    "SAP Human Resources",
    "SAP Payroll",
    "SAP Labor Distribution",
    "SAP Plant Maintenance",
    "Electronic Messaging",
    "Email",
    "Outlook Web Access (OWA)",
    "Blackberry",
    "Windows Mobile",
    "IT Services",
    "Retail",
    "Retail POS (Point of Sale)",
    "Retail Client Registration",
    "Retail Client Lookup",
    "Retail Adding Points",
    "E-Commerce",
    "DNB Enterprise Services",
    "Jive Enterprise Services",
    "PeopleSoft Enterprise Services",
    "PeopleSoft CRM",
    "PeopleSoft Supply Chain Management",
    "PeopleSoft Asset Lifecycle Management",
    "PeopleSoft Financials",
    "PeopleSoft HRMS",
    "PeopleSoft Portals",
    "PeopleSoft Governance",
    "PeopleSoft Reporting",
    "Tableau Enterprise Services",
    "Saba Enterprise Services",
    "SAP SuccessFactors",
    "Bond Trading",
    "Shared Storage (SAN)",
    "Concur Enterprise Travel & Expense Services",
    "ADP Enterprise Services",
    "OpenText Enterprise Services",
    "LinkedIn Enterprise Services",
    "Client Services",
    "Securities Lending",
    "Bond Trading - DR",
    "OOYALA Enterprise Services",
    "Workday Enterprise Services",
    "Adobe Enterprise Services",
    "SalesForce Enterprise Services",
    "ServiceNow Enterprise Services",
    "Fidelity Enterprise Services",
    "Total User Management",
    "Google Enterprise Services",
    "Sales Force Automation",
    "Oracle Eloqua Enterprise Services",
    "TopQuadrant Enterprise Services",
    "Slack",
    "Oracle Enterprise Services",
    "Jobvite Enterprise Recruitment Services",
    "This Service-now instance",
    "Apache Web Hosting",
    "Oracle Taleo Enterprise Services",
    "Okta Enterprise Services",
    "insidesales.com Enterprise Services"
]

# Incident types for different service categories
incident_types = {
    "performance": [
        "Slow performance", "Response time degradation", "Timeout errors",
        "High latency", "Performance degradation", "System sluggish"
    ],
    "access": [
        "Login failed", "Access denied", "Authentication error",
        "Permission issues", "User access problems", "SSO failure"
    ],
    "functionality": [
        "Feature not working", "Button not responding", "Form submission failed",
        "Report generation error", "Search not functioning", "Export failed"
    ],
    "connectivity": [
        "Connection timeout", "Service unavailable", "Network connectivity issues",
        "API failure", "Integration error", "Sync problems"
    ],
    "data": [
        "Data not loading", "Incorrect data displayed", "Data sync failure",
        "Missing records", "Data corruption", "Database connection failed"
    ],
    "ui": [
        "UI rendering issues", "Display problems", "Layout broken",
        "Styling errors", "Mobile responsiveness issues"
    ]
}

states = ["New", "In Progress", "Resolved"]
priorities = ["Low", "Medium", "High", "Critical"]

# Resolution codes for resolved incidents
resolution_codes = [
    "Duplicate", "Known error", "No resolution provided", "Resolved by caller",
    "Resolved by change", "Resolved by problem", "Resolved by request",
    "Solution provided", "Workaround provided", "User error"
]

# Close notes templates for different resolution codes
close_notes_templates = {
    "Duplicate": [
        "Duplicate of existing incident {inc_number}. Closing as duplicate.",
        "This issue was already reported in {inc_number}. Marking as duplicate.",
        "Duplicate ticket - original incident {inc_number} already addresses this issue."
    ],
    "Known error": [
        "This is a known issue with documented workaround. Reference knowledge article KA{ka_id}.",
        "Known system limitation. Engineering team aware and working on permanent fix.",
        "Known error - temporary workaround applied until permanent solution is deployed."
    ],
    "No resolution provided": [
        "Unable to reproduce the issue. No further action required at this time.",
        "User unresponsive to follow-up attempts. Closing incident.",
        "Issue could not be verified. No resolution provided."
    ],
    "Resolved by caller": [
        "Caller reported issue resolved itself. No further action needed.",
        "User found alternative solution. Incident resolved by caller.",
        "Caller indicated the problem is no longer occurring."
    ],
    "Resolved by change": [
        "Issue resolved by change request CHG{change_id}. System update addressed the problem.",
        "Recent system change fixed the reported issue. Change {change_id} successfully implemented.",
        "Deployment of patch resolved the incident. Change management ticket CHG{change_id}."
    ],
    "Resolved by problem": [
        "Root cause identified and resolved via problem ticket PRB{problem_id}.",
        "Underlying problem addressed through problem management. Reference PRB{problem_id}.",
        "Permanent fix implemented via problem record {problem_id}."
    ],
    "Resolved by request": [
        "Resolution provided as requested by user. All requirements met.",
        "Service request fulfilled as specified. Incident closed.",
        "User's specific request completed successfully."
    ],
    "Solution provided": [
        "Step-by-step solution provided to user. Issue resolved.",
        "Technical solution implemented. User confirmed resolution.",
        "Configuration update resolved the issue. Solution documented."
    ],
    "Workaround provided": [
        "Temporary workaround provided to restore service. Permanent fix pending.",
        "User instructed on workaround procedure. Service restored temporarily.",
        "Workaround implemented while engineering develops permanent solution."
    ],
    "User error": [
        "User education provided on proper procedure. Issue resolved.",
        "Training gap identified. User guided through correct process.",
        "Misconfiguration corrected. User now able to proceed successfully."
    ]
}

# Detailed description templates
description_templates = [
    "Users reporting {issue} with {service} affecting daily operations",
    "System alert: {issue} detected in {service} environment",
    "Multiple users experiencing {issue} when using {service}",
    "Critical incident: {issue} impacting {service} functionality",
    "Performance monitoring detected {issue} in {service}",
    "User complaints about {issue} while accessing {service}",
    "Service degradation: {issue} affecting {service} availability",
    "Technical issue: {issue} preventing normal use of {service}",
    "Outage reported: {issue} causing service interruption for {service}",
    "Integration problem: {issue} between {service} and other systems"
]

# Generate unique INC numbers
def generate_inc_number(incident_id):
    base_number = incident_id + random.randint(1000, 9999)
    inc_number = base_number % 10000000
    return f"INC{inc_number:07d}"

def generate_close_notes(resolution_code, inc_number):
    template = random.choice(close_notes_templates[resolution_code])
    
    # Replace placeholders with realistic values
    if "{inc_number}" in template:
        # Generate a different incident number for duplicate references
        ref_inc = random.randint(1000, 9999)
        template = template.format(inc_number=f"INC{ref_inc:07d}")
    elif "{ka_id}" in template:
        template = template.format(ka_id=random.randint(10000, 99999))
    elif "{change_id}" in template:
        template = template.format(change_id=random.randint(1000, 9999))
    elif "{problem_id}" in template:
        template = template.format(problem_id=random.randint(1000, 9999))
    
    return template

def generate_dates(state):
    # Created date in the last 90 days
    created_days_ago = random.randint(0, 90)
    created_date = datetime.now() - timedelta(days=created_days_ago)
    
    # Updated date logic based on state
    if state == "New":
        # For new tickets, updated date is same as created date (or very close)
        updated_date = created_date + timedelta(minutes=random.randint(0, 60))
    elif state == "In Progress":
        # For in progress tickets, updated date is between 1 hour and 30 days after created date
        days_difference = random.randint(0, 30)
        hours_difference = random.randint(1, 23)
        minutes_difference = random.randint(0, 59)
        updated_date = created_date + timedelta(
            days=days_difference, 
            hours=hours_difference, 
            minutes=minutes_difference
        )
        # Ensure updated date doesn't exceed current date
        if updated_date > datetime.now():
            updated_date = datetime.now() - timedelta(hours=random.randint(1, 12))
    else:  # Resolved
        # For resolved tickets, updated date is between 1 day and 60 days after created date
        days_difference = random.randint(1, 60)
        hours_difference = random.randint(1, 23)
        minutes_difference = random.randint(0, 59)
        updated_date = created_date + timedelta(
            days=days_difference, 
            hours=hours_difference, 
            minutes=minutes_difference
        )
        # Ensure updated date doesn't exceed current date
        if updated_date > datetime.now():
            updated_date = datetime.now() - timedelta(hours=random.randint(1, 12))
    
    return created_date, updated_date

def generate_incident(incident_id):
    service = random.choice(services)
    incident_category = random.choice(list(incident_types.keys()))
    issue_type = random.choice(incident_types[incident_category])
    
    # Generate INC number
    inc_number = generate_inc_number(incident_id)
    
    # Create short description
    short_description = f"{service.split()[0]} {issue_type}"
    
    # Create detailed description
    description_template = random.choice(description_templates)
    description = description_template.format(issue=issue_type.lower(), service=service)
    
    state = random.choice(states)
    priority = random.choice(priorities)
    
    # Generate created and updated dates
    created_date, updated_date = generate_dates(state)
    
    # Generate random impact and urgency
    impact = random.choice(["Low", "Medium", "High", "Critical"])
    urgency = random.choice(["Low", "Medium", "High", "Critical"])
    
    # For resolved incidents, add resolution code and close notes
    resolution_code = ""
    close_notes = ""
    
    if state == "Resolved":
        resolution_code = random.choice(resolution_codes)
        close_notes = generate_close_notes(resolution_code, inc_number)
    
    return [
        inc_number,  # INC number as the first column
        incident_id,  # Keep sequential ID for reference
        short_description,
        description,
        service,
        incident_category.capitalize(),
        state,
        priority,
        impact,
        urgency,
        created_date.strftime("%Y-%m-%d %H:%M:%S"),
        updated_date.strftime("%Y-%m-%d %H:%M:%S"),
        resolution_code,
        close_notes
    ]

# Generate 10,000 records
print("Generating 10,000 incident records with resolution codes and close notes...")
print(f"Total services available: {len(services)}")

with open('incidents_10000.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write header with new resolution fields
    writer.writerow([
        'inc_number', 'id', 'short_description', 'description', 'service', 
        'incident_category', 'state', 'priority', 'impact', 
        'urgency', 'created_date', 'updated_date', 'resolution_code', 'close_notes'
    ])
    
    # Write 10,000 records
    for i in range(1, 10001):
        if i % 1000 == 0:
            print(f"Generated {i} records...")
        writer.writerow(generate_incident(i))

print("File 'incidents_10000.csv' created successfully with 10,000 records!")
print(f"Services used: {len(services)} different enterprise services")
print("INC numbers format: INC followed by 7 digits (e.g., INC0001234)")
print("Resolution codes and close notes added for resolved incidents")
