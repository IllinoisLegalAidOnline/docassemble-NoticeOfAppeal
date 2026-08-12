def paper_filing_option(user, delivery_parties):
    if user.has_email_address:
      return False
    for party in delivery_parties:
      if party.knows_delivery_method and (party.email_delivery or party.efm_delivery):
        return False
    return True