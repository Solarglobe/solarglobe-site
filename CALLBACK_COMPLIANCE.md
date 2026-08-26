# Conformité des demandes de rappel SolarGlobe

Date : 26/08/2026

Ce dépôt contient le site public statique. Il ne contient pas le CRM d’appel ni le backend de scoring des prospects achetés. Les formulaires publics ont été durcis pour transmettre une preuve minimale horodatable, mais le blocage opérationnel des appels doit être implémenté dans le CRM qui consomme ces demandes.

## Payload minimal attendu

- request_id
- lead_id
- consumer_name
- phone_number
- request_timestamp
- source_type
- source_url
- form_version
- exact_request_text
- requested_services
- callback_deadline
- evidence_status
- partner_name
- partner_evidence_id
- proof_file_or_snapshot
- proof_hash
- withdrawn_at
- do_not_call
- created_at
- updated_at

## Texte exact de demande de rappel

Je demande expressément à SolarGlobe de me rappeler au sujet de mon projet photovoltaïque et des services que j’ai sélectionnés.

## Statuts CRM requis

- callback_request_valid
- existing_contract
- proof_missing
- expired
- withdrawn
- do_not_call
- legal_review_required

## Règles d’appel

`callback_deadline = demande + 5 jours ouvrables`, fuseau Europe/Paris. Le samedi compte comme jour ouvrable, le dimanche et les jours fériés habituellement non travaillés ne comptent pas. Le calcul commence le jour ouvrable suivant la demande.

Téléphone bloqué si statut : `proof_missing`, `expired`, `withdrawn`, `do_not_call`, `legal_review_required`. Tout déblocage manuel doit être journalisé avec utilisateur, date, justification et preuve.

## Prospects achetés

Un fichier contenant seulement nom, téléphone et opt-in oui ne suffit pas. Si SolarGlobe n’est pas clairement identifiable dans la preuve, classer le prospect en `legal_review_required`. Les anciens prospects sans preuve exploitable doivent rester `proof_missing`.
